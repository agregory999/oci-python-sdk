##########################################################################
# fss_backup.py
#
# @author: Andrew Gregory, June 2022
#
# Supports Python 3
#
# This script is designed to create Object-storage-based backups of OCI FileSystems
# The intent is that users would run this via cron, and it will create a synchronized
# copy of the filesystem using rclone out on OSS.  The notion of a "daily"
# backup uses the concpet of object versioning, whilst a "weekly" or "monthly" is a point-in-time
# cut and is immutable.
# When used in conjunction with Object Lifecycle Rules, it can create automatic self-maintaining
# replicas of the file system in a non-FSS manner.
#
##########################################################################
# Application Command line parameters
#
#   -h, --help            show this help message and exit
#   -v, --verbose         increase output verbosity
#   -fs FSSOCID, --fssocid FSSOCID
#                         FSS Compartment OCID of doing a single FS
#   -fc FSSCOMPARTMENT, --fsscompartment FSSCOMPARTMENT
#                         FSS Compartment OCID
#   -oc OSSCOMPARTMENT, --osscompartment OSSCOMPARTMENT
#                         OSS Backup Comaprtment OCID
#   -r REMOTE, --remote REMOTE
#                         Named rclone remote for that user. ie oci:
#   -ad AVAILABILITYDOMAIN, --availabilitydomain AVAILABILITYDOMAIN
#                         AD for FSS usage. Such as dDzb:US-ASHBURN-AD-1
#   -m MOUNTOCID, --mountocid MOUNTOCID
#                         Mount Point OCID to use.
#   -pr PROFILE, --profile PROFILE
#                         OCI Profile name (if not default)
#   -ty TYPE, --type TYPE
#                         Type: daily(def), weekly, monthly
#   --dryrun              Dry Run - print what it would do
#   -ssc, --serversidecopy
#                         For weekly/monthly only - copies directly from latest daily backup, not source FSS
#   -s, --sortbytes       Sort by byte size of FSS, smallest to largest (smaller FS backed up first
#   -t THRESHOLD, --threshold THRESHOLD
#                         GB threshold - do not back up share if more than this
#
#
##########################################################################

import time
import datetime
import os
import signal
import subprocess
import multiprocessing
import argparse
import sys
import logging

import oci
from oci.auth.signers import InstancePrincipalsSecurityTokenSigner

#######################################
# CONSTANTS
SNAPSHOT_NAME = "FSS-dailyBackup"

# File system temporary Mount Point
TEMP_MOUNT = "/mnt/temp-backup"

# Threshold GB (Don't back up if > this)
THRESHOLD_GB = sys.maxsize

# Number of cores (like nproc)
CORE_COUNT = multiprocessing.cpu_count()

# Define globally but set later
verbose = False

# Set the logger
logger = logging.getLogger('fss-backup')

#######################################
# SUB ROUTINES


def extract_bytes(file_system):
    """Pull out file system byte count"""
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".
        return int(file_system.metered_bytes)
    except KeyError:
        return 0


def cleanup_file_snapshot(fs_client, fs_ocid):
    """Use API to attempt bucket creation"""

    # Use API to attempt bucket creation
    snapshots = fs_client.list_snapshots(file_system_id=fs_ocid)
    for snap in snapshots.data:
        if snap.name == SNAPSHOT_NAME:
            logger.debug(f"Deleting old Snapshot {SNAPSHOT_NAME} with OCID: {snap.id}")
            file_storage_client.delete_snapshot(snapshot_id=snap.id)
            logger.debug("Sleeping 5sec to allow deletion to complete")
            time.sleep(5)
            return


def cleanup_temporary_mount(named_mount):
    """Quietly ensures we have a clean mount point"""
    try:
        if named_mount:
            # Try to unmount named mount first if set
            os_command = ["sudo"] if use_sudo else []
            os_command.extend(["umount", "-f", named_mount])
            logger.debug(f'Running OS Command: {" ".join(os_command)}')
            completed_process = subprocess.run(os_command, shell=False, check=True, capture_output=True, text=True)
            logger.debug(f"OS Command Output: {completed_process}")
        # Try to unmount generic mount first if nothing else
        os_command = ["sudo"] if use_sudo else []
        os_command.extend(["umount", "-f", TEMP_MOUNT])
        logger.debug(f'Running OS Command: {" ".join(os_command)}')
        completed_process = subprocess.run(os_command, shell=False, capture_output=True, text=True)
        logger.debug(f"OS Command Output: {completed_process}")
    except subprocess.CalledProcessError as err:
        logger.debug(f"OS: umount failed with return code {err.returncode} and STDERR {err.stderr} but this is ok")


def ensure_temporary_mount():
    """If mount doesn't exist"""
    if not os.path.isdir(TEMP_MOUNT):
        # Attempt create and fail if we cannot
        try:
            os.makedirs(TEMP_MOUNT)
        except Exception as ex:
            # Raise because if we cannot, we should kill the script immediately
            raise ex


def ensure_backup_bucket(oss_client, bucket) -> bool:
    """Check bucket status - create if necessary"""
    try:
        object_storage_client.get_bucket(namespace_name=namespace_name, bucket_name=bucket)
        logger.debug(f"Bucket {bucket} found")
    except oci.exceptions.ServiceError:
        logger.debug(f"Bucket {bucket} not found - creating")
        if not dry_run:
            # Fix for bucket creation error - try and catch oci.exceptions.ServiceError
            try:
                # Create a new bucket
                oss_client.create_bucket(
                    namespace_name=namespace_name,
                    create_bucket_details=oci.object_storage.models.CreateBucketDetails(
                        name=bucket,
                        compartment_id=oss_compartment_ocid,
                        storage_tier="Standard",
                        object_events_enabled=True,
                        versioning="Enabled"
                    )
                )
            except oci.exceptions.ServiceError as ex:
                logger.error(f"Unable to create backup bucket {bucket}: {ex.message}")
                return False
        else:
            logger.info(f"Dry Run: Would have created bucket {bucket} in compartment {oss_compartment_ocid}")
    # True means we are ok to proceed
    return True


def get_suitable_export(file_storage_client, virtual_network_client, mt_ocid, fs_ocid):
    """Grab the list of exports from MT and iterate. Pick one with the right mount IP and return it"""

    mount_target = file_storage_client.get_mount_target(mount_target_id=mt_ocid)
    mount_ip = virtual_network_client.get_private_ip(private_ip_id=mount_target.data.private_ip_ids[0])
    logger.debug(f"MT IP: {mount_ip.data.ip_address} ID {mount_target.data.id}")

    # Iterate And grab first suitable export
    exports = file_storage_client.list_exports(export_set_id=mount_target.data.export_set_id)
    for export in exports.data:
        if export.file_system_id == fs_ocid:
            logger.debug(f"MT {mount_ip.data.ip_address} Found {export.id} with path {export.path}")
            return f"{mount_ip.data.ip_address}:{export.path}"
    # Nothing suitable
    raise ValueError("Cannot find any matching exports")


def mount_ro_filesystem() -> bool:
    """Mount the file system using temporary mount point"""
    try:
        mount_command = ["sudo"] if use_sudo else []
        mount_command.extend(['mount', "-r", f"{mount_path}", f"{TEMP_MOUNT}"])
        logger.debug(f'OS Command: {" ".join(mount_command)}')
        completed_process = subprocess.run(mount_command, shell=False, check=True, capture_output=True, text=True)
        logger.debug(f"OS Command output: {completed_process}")
    except subprocess.CalledProcessError as exc:
        logger.error(f"Unable to mount {mount_path} to {TEMP_MOUNT}. Return code {exc.returncode}, Output: {exc.stderr}")
        logger.debug(exc)
        return False
    return True


def synchronize_tags(file_storage_client, object_storage_client, fs_ocid, oss_namespace, backup_bucket_name):
    # Grab all tags for FSS
    fs_ref = file_storage_client.get_file_system(file_system_id=fs_ocid).data
    fs_defined_tags = fs_ref.defined_tags
    fs_freeform_tags = fs_ref.freeform_tags
    # Get all tags for OSS bucket
    bucket_ref = object_storage_client.get_bucket(namespace_name=oss_namespace,
                                                  bucket_name=backup_bucket_name).data
    bucket_defined_tags = bucket_ref.defined_tags
    bucket_freeform_tags = bucket_ref.freeform_tags
    logger.debug(f"Filesystem {fs_ref.display_name} Defined Tags: {fs_defined_tags}")
    logger.debug(f"Filesystem {fs_ref.display_name} Freeform Tags: {fs_freeform_tags}")
    logger.debug(f"Bucket {bucket_ref.name} Defined Tags: {bucket_defined_tags}")
    logger.debug(f"Bucket {bucket_ref.name} Freeform Tags: {bucket_freeform_tags}")
    # Build Defined Tags for OSS Bucket, start with empty JSON
    for ns in autotag_ns_list:
        # Iterate Tag Namespaces to sync, catch KeyError and ignore
        try:
            # Grab all tags for FSS
            if fs_defined_tags[ns]:
                logger.info(f"Adding NS from FSS: {ns} to tags")
                bucket_defined_tags[ns] = fs_defined_tags[ns]
        except KeyError as exc:
            # Ignore but log
            logger.info(f"No FSS tags for NS {ns}: {exc}, ignoring.")

    # Just add a freeform tag to indicate this is automatically updated
    bucket_freeform_tags["AUTOTAG"] = f"DO NOT UPDATE TAGS - These were automatically synced {datetime.datetime.now()}"
    logger.info(f'Defined Tags to set on OSS Bucket {backup_bucket_name}: {bucket_defined_tags}')
    logger.info(f'Freeform Tags to set on OSS Bucket {backup_bucket_name}: {bucket_freeform_tags}')
    # Update bucket

    bucket_update = oci.object_storage.models.UpdateBucketDetails(defined_tags=bucket_defined_tags,
                                                                  freeform_tags=bucket_freeform_tags)
    # API Call
    if dry_run:
        logger.info(f"DRY RUN: Would update bucket with: {bucket_update}")
    else:
        # Real
        oss_response = object_storage_client.update_bucket(namespace_name=oss_namespace,
                                                            bucket_name=backup_bucket_name,
                                                            update_bucket_details=bucket_update).data
        # Check for success
        logger.info(f"Verify Bucket {backup_bucket_name} Defined Tags: {oss_response.defined_tags}")


def signal_handler(signum, frame):
    logger.warning(f"Caught signal {signum} from OS.  Cleaning up file mount before exit.")
    cleanup_temporary_mount(None)
    print("Exit")
    exit(1)


######################################
#  MAIN ROUTINE

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-fs", "--fssocid", help="FSS Compartment OCID of doing a single FS")
parser.add_argument("-fc", "--fsscompartment", help="FSS Compartment OCID", required=True)
parser.add_argument("-oc", "--osscompartment", help="OSS Backup Comaprtment OCID", required=True)
parser.add_argument("-r", "--remote", help="Named rclone remote for that user.  ie oci:", required=True)
parser.add_argument("-ad", "--availabilitydomain",
                    help="AD for FSS usage.  Such as dDzb:US-ASHBURN-AD-1",
                    required=True)
parser.add_argument("-m", "--mountocid", help="Mount Point OCID to use.", required=True)
parser.add_argument("-pr", "--profile", type=str, help="OCI Profile name (if not default)", default="DEFAULT")
parser.add_argument("-ty", "--type", type=str, help="Type: daily(def), weekly, monthly", default="daily")
parser.add_argument("--dryrun", help="Dry Run - print what it would do", action="store_true")
parser.add_argument("-ssc", "--serversidecopy",
                    help="For weekly/monthly only - copies directly from latest daily backup, not source FSS",
                    action="store_true")
parser.add_argument("-s", "--sortbytes",
                    help="Sort by byte size of FSS, smallest to largest (smaller FS backed up first",
                    action="store_true")
parser.add_argument("-t", "--threshold", help="GB threshold - do not back up share if more than this", type=int)
parser.add_argument("-su", "--usesudo", help="Attempt to run mount/umount with sudo - requires /etc/sudoers", action="store_true")
parser.add_argument("-ip", "--instanceprincipal", help="Use Instance Principal Auth - negates --profile", action="store_true")
parser.add_argument("-a", "--autotag", help="Automatically tag backup bucket with all tags from specified namespaces. Specify like so:  -a NS1 NS2", nargs="+")
parser.add_argument("--archivetier", help="Send Weekly/Monthly archives directly to archive tier. Does not apply to SSC", action="store_true")
args = parser.parse_args()

# Process boolean arguments
verbose = args.verbose
use_sudo = args.usesudo
dry_run = args.dryrun
server_side_copy = args.serversidecopy
sort_bytes = args.sortbytes
use_instance_principals = args.instanceprincipal
profile = args.profile
autotag_ns_list = args.autotag
additional_backups_archive_tier = args.archivetier

# FSS Compartment OCID
fss_compartment_ocid = args.fsscompartment if args.fsscompartment else None

# FSS Single OCID
fss_ocid = args.fssocid if args.fssocid else None

# OSS Compartment OCID
oss_compartment_ocid = args.osscompartment if args.osscompartment else None

# Mount IP
mt_ocid = args.mountocid

# RCLONE Remote
rclone_remote = args.remote

# Type (daily, weekly, monthly)
backup_type = args.type

# Availability Domain
fss_avail_domain = args.availabilitydomain

# FSS Threshold
threshold_gb = args.threshold if args.threshold else THRESHOLD_GB

# Set the log level to DEBUG or INFO
if verbose:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
logging.info(f"Initialized Logger: {logger}")

# Define Signal Handler for cleanup
signal.signal(signal.SIGINT, signal_handler)
logger.info("Created Signal Handler for ^C")

# Define OSS clients
if use_instance_principals:
    logger.info("Using Instance Principal Authentication")
    signer = InstancePrincipalsSecurityTokenSigner()
    object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    file_storage_client = oci.file_storage.FileStorageClient(config={}, signer=signer)
    virtual_network_client = oci.core.VirtualNetworkClient(config={}, signer=signer)
else:
    # Use a profile (must be defined)
    logger.info(f"Using Profile Authentication: {profile}")
    config = oci.config.from_file(profile_name=profile)

    object_storage_client = oci.object_storage.ObjectStorageClient(config)
    file_storage_client = oci.file_storage.FileStorageClient(config)
    virtual_network_client = oci.core.VirtualNetworkClient(config)

# Sleep for a few seconds before beginning
time.sleep(1)

# Get Object namespace
namespace_name = object_storage_client.get_namespace().data

# Try to see if mount is there and clean - die if not (raise unchecked)
try:
    # If we can't have the mount, kill the script
    ensure_temporary_mount()
    # Now clean it up if it is mounted
    cleanup_temporary_mount(None)
except FileExistsError as exc:
    logger.critical(f"FATAL: No way to use mount point {TEMP_MOUNT}: {exc}")
    exit(1)

# Explain what we are doing
if backup_type in ['weekly', 'monthly']:
    logger.info(f'Performing Daily Incremental Backup AND {backup_type} using {"Server-Side Copy" if server_side_copy else "Rclone Copy"} method {" direct to Archive tier" if additional_backups_archive_tier else " to Standard tier"}')
else:
    logger.info('Performing Daily Incremental Backup')

# Print threshold if set
if threshold_gb < sys.maxsize:
    # This means it was set to anything
    logger.info(f"GB Threshold set to {threshold_gb} GB - will skip any FS larger than this")

# Set Start timer
start = time.time()

# Main loop - list File Shares

# For listing, if the fss_ocid is set to a single FS, only do that in the filter
# Else get all shares
if fss_ocid:
    shares = file_storage_client.list_file_systems(compartment_id=fss_compartment_ocid,
                                                   availability_domain=fss_avail_domain,
                                                   id=fss_ocid,
                                                   lifecycle_state="ACTIVE")
else:
    shares = file_storage_client.list_file_systems(compartment_id=fss_compartment_ocid,
                                                   availability_domain=fss_avail_domain,
                                                   lifecycle_state="ACTIVE")

# At this point iterate the list (even if single)
logger.info(f'{f"Using {fss_ocid} in" if fss_ocid else "Iterating filesystems in"} Compartment: \
{fss_compartment_ocid}.  Count: {len(shares.data)}')

# Sort by smallest to largest
if sort_bytes:
    logger.debug("Sorting FSS List smallest to largest")
    shares.data.sort(key=extract_bytes)

for share in shares.data:
    logger.info(f"Share name: {share.display_name} Size: {round(share.metered_bytes/(1024*1024*1024), 2)} GB")
    backup_bucket_name = share.display_name.strip("/") + "_backup"
    # Check size and skip this filesystem if it exceeds threshold
    if (share.metered_bytes > (threshold_gb * 1024 * 1024 * 1024)):
        logger.info(f"File System is {round(share.metered_bytes/(1024*1024*1024), 2)} GB.  Threshold is {threshold_gb} GB.  Skipping")
        continue

    # Ensure that the bucket is there, create otherwise
    bucket_exists = ensure_backup_bucket(oss_client=object_storage_client,
                                         bucket=backup_bucket_name)

    # For for no available bucket
    if not bucket_exists:
        logger.warning(f"Bucket {backup_bucket_name} is not available for share {share.display_name}. Continuing.")
        continue

    # Auto-tag feature
    if autotag_ns_list and len(autotag_ns_list) > 0:
        logger.debug(f"Auto-tagging bucket {backup_bucket_name} start")
        synchronize_tags(file_storage_client=file_storage_client,
                         object_storage_client=object_storage_client,
                         fs_ocid=share.id,
                         oss_namespace=namespace_name,
                         backup_bucket_name=backup_bucket_name)
        logger.debug(f"Auto-tagging bucket {backup_bucket_name} complete")

    # Try mount and rclone, it not, clean up snapshot
    try:    # Overall try/catch/finally

        # Call the helper to get export path and mount
        try:
            # Get the export we will use, do not continue if we cannot
            mount_path = get_suitable_export(file_storage_client, virtual_network_client,
                                                mt_ocid=mt_ocid, fs_ocid=share.id)
            logger.debug(f"Using the following mount path: {mount_path}")
        except ValueError as exc:
            logger.error("No Suitable Mount point. Continue to next share")
            logger.debug(exc)
            continue

        # Call out to OS to mount RO - try to continue if fail
        if not dry_run:
            # Mount command
            did_mount = mount_ro_filesystem()
            if not did_mount:
                logger.warning(f"Didnt mount {mount_path} to {TEMP_MOUNT}. Skipping")
                continue
        else:
            logger.info(f'Dry Run: {"sudo " if use_sudo else ""}mount -r {mount_path} {TEMP_MOUNT}')

        # FSS Snapshot (for clean backup) - only do if is the mount was successful
        try:    # Catch API Error
            if not dry_run:
                # Try to delete FSS Snapshot - ok if it fails
                logger.debug(f"Cleanup FSS Snapshot for {share.id}")
                cleanup_file_snapshot(fs_client=file_storage_client, fs_ocid=share.id)
                logger.debug(f"Creating FSS Snapshot: {SNAPSHOT_NAME} via API")
                snapstart = time.time()
                snapshot = file_storage_client.create_snapshot(
                    create_snapshot_details=oci.file_storage.models.CreateSnapshotDetails(
                        file_system_id=share.id,
                        name=SNAPSHOT_NAME)
                )
                snapend = time.time()
                logger.debug(f"FSS Snapshot time(ms): {(snapend - snapstart):.2f}s OCID: {snapshot.data.id}")
            else:
                logger.info(f"Dry Run: Create FSS Snapshot {SNAPSHOT_NAME} via API")
        except oci.exceptions.RequestException as exc:
            logger.error("API Failed. Continue to cleanup mount")
            logger.debug(exc)
            continue

        # Now that we have a mount and a snapshot, continue with rclone
        try:
            # Define remote path on OSS
            remote_path = f"{rclone_remote}{backup_bucket_name}/{SNAPSHOT_NAME}"
            additional_copy_name = f"FSS-{backup_type}Backup-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
            additional_remote_path = f"{rclone_remote}{backup_bucket_name}/{additional_copy_name}"
            rclone_daily_command = ["rclone", "sync",
                                    "--stats-one-line",
                                    "--metadata",
                                    "--links",
                                    "--oos-chunk-size=32M",
                                    f"--oos-upload-concurrency={CORE_COUNT}",
                                    f"--transfers={CORE_COUNT}",
                                    f"--checkers={CORE_COUNT*3}",
                                    f"/mnt/temp-backup/.snapshot/{SNAPSHOT_NAME}",
                                    f"{remote_path}"
                                    ]
            rclone_additional_command = ["rclone", "copy",
                                          "--stats-one-line",
                                          "--no-check-dest",
                                          "--metadata",
                                          "--links",
                                          "--oos-chunk-size=32M",
                                          f"--oos-upload-concurrency={CORE_COUNT}",
                                          f"--transfers={CORE_COUNT}",
                                          f"--checkers={CORE_COUNT*3}",
                                          f"/mnt/temp-backup/.snapshot/{SNAPSHOT_NAME}",
                                          f"{additional_remote_path}"
                                          ]
            rclone_additional_command_ssc = ["rclone", "copy",
                                              "--stats-one-line",
                                              "--no-check-dest",
                                              f"--transfers={CORE_COUNT*2}",
                                              f"--checkers={CORE_COUNT*3}",
                                              f"{remote_path}",
                                              f"{additional_remote_path}"]
            if additional_backups_archive_tier:
                rclone_additional_command.append("--oos-storage-tier")
                rclone_additional_command.append("Archive")
            if verbose:
                rclone_daily_command.append("-vv")
                rclone_additional_command.append("-vv")
                rclone_additional_command_ssc.append("-vv")
            else:
                rclone_daily_command.append("-v")
                rclone_additional_command.append("-v")
                rclone_additional_command_ssc.append("-v")        
            # If Dry Run, print and move on
            if dry_run:
                # Print Daily Commands
                logger.info(f"Dry Run: Using Remote Path (rclone_remote:bucket/snapshot): {rclone_remote}{backup_bucket_name}/{SNAPSHOT_NAME}")
                logger.info(f"Dry Run: rclone daily command: {rclone_daily_command}")
                if backup_type in ['weekly', 'monthly']:
                    if server_side_copy:
                        logger.info(f"Dry Run: rclone weekly/monthly SSC command: rclone copy -v {remote_path} {additional_remote_path}")
                    else:
                        logger.info(f"Dry Run: rclone weekly/monthly direct command: {rclone_additional_command}")

            else:
                logger.debug(f"Using Remote Path (rclone_remote:bucket/snapshot): {rclone_remote}{backup_bucket_name}/{SNAPSHOT_NAME}")

                # Call out to rclone it
                # Additional flags to consider
                # --s3-disable-checksum  only for large objects, avoid md5sum which is slow
                # --checkers = Core Count * 2
                try:
                    logger.info(f'Calling RCLONE daily with {" ".join(rclone_daily_command)}')
                    # Run the Daily backup
                    completed = subprocess.run(rclone_daily_command, shell=False, check=True, capture_output=True, text=True)
                    #logger.debug(f"RCLONE STDOUT: {completed.stdout}")
                    logger.info(f"RCLONE Daily Backup returned: \n{completed.stderr}")
                    if completed.returncode != 0:
                        logger.debug(f"RCLONE Return code {completed.returncode} STDERR: {completed.stderr}")
                    # Additional Backup if weekly or monthly selected.  Options are Direct Copy or Server Side Copy
                    if backup_type in ['weekly', 'monthly']:
                        if server_side_copy:
                            logger.info(f'Creating additional {backup_type} backup called {additional_copy_name}. Implemented as rclone server side copy')
                            logger.info(f'Calling RCLONE {backup_type} with {" ".join(rclone_additional_command_ssc)}')
                            completed = subprocess.run(rclone_additional_command_ssc, shell=False, check=True, capture_output=True, text=True)
                            logger.info(f"RCLONE {backup_type} SSC returned: \n{completed.stderr}")
                            if completed.returncode != 0:
                                logger.debug(f"RCLONE Return code {completed.returncode} STDERR: {completed.stderr}")
                        else:
                            # Direct Copy
                            logger.info(f'Creating additional {backup_type} backup called {additional_copy_name}. Implemented as rclone Direct Copy from FSS (full)')
                            logger.info(f'Calling RCLONE {backup_type} with {" ".join(rclone_additional_command)}')
                            completed = subprocess.run(rclone_additional_command, shell=False, check=True, capture_output=True, text=True)
                            logger.info(f"RCLONE {backup_type} Direct returned: \n{completed.stderr}")
                            if completed.returncode != 0:
                                logger.debug(f"RCLONE Return code {completed.returncode} STDERR: {completed.stderr}")
                except subprocess.CalledProcessError as exc:
                    logger.warning("rclone failed. Continue processing to remove snapshot and clean up")
                    logger.debug(exc)

            # Delete Snapshot - no need to keep at this point
            if not dry_run:
                logger.debug(f"Deleting Snapshot from FSS. Name: {snapshot.data.name} OCID:{snapshot.data.id}")
                try:
                    file_storage_client.delete_snapshot(snapshot_id=snapshot.data.id)
                except oci.exceptions.RequestException as ex:
                    logger.warning(f"Deletion of FSS Snapshot failed.  Please record OCID: {snapshot.data.id} and delete manually.")
                    logger.debug(ex)
            else:
                logger.info(f"Dry Run: Delete Snapshot from FSS: {SNAPSHOT_NAME}")
        # Catching API errors from mount issue or snapshot creation/deletion
        except oci.exceptions.RequestException as exc:
            logger.error("API Failed. Continue to cleanup mount")
            logger.debug(exc)
        except ValueError as exc:
            logger.error("No Export. Continue processing")
            logger.debug(exc)
        
        # End of main routine
        # Catch exceptions
    except Exception as exc:
        logger.warning("ERROR: Generic Exception. Continue processing")
        logger.debug(exc)
    finally:
        logger.debug("Executing mount cleanup in finally block")
        # Unmount File System (Cleanup)
        try:
            if not dry_run:
                cleanup_temporary_mount(mount_path)
            else:
                logger.info(f"Dry Run (Finally): umount -f {mount_path}")
        except Exception as exc:
            logger.debug("Unable to unmount. Continue to next share")
            logger.debug(exc)

end = time.time()
logger.info(f"Finished | Time taken: {(end - start):.2f}s")
