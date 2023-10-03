##########################################################################
# oci-sync-defined-tags-fss-oss.py.py
#
# @author: Andrew Gregory, September 2023
#
# Supports Python 3
#
# This script synchronizes the named Tag Namespaces that apply to FSS onto OSS.  Assuming
# the same FSS -> OSS Backup structure with a named bucket per FSS Share:
#
# FSS Share named abc -> OSS bucket named abc_backup
#
# The script leaves alone all freeform tags on the OSS Bucket and also all Defined tags in
# other namespaces.  
# 
# Example run 1 - Sync all tags in XX Namespace:
# python3 ./oci-sync-defined-tags-fss-oss.py -ad UWQV:US-ASHBURN-AD-3 -oc ocid1.compartment.oc1..zz -fc ocid1.compartment.oc1..zz -a XX
#
# Example run 2 - Sync all tags in XX and YY Namespace:
# python3 ./oci-sync-defined-tags-fss-oss.py -ad UWQV:US-ASHBURN-AD-3 -oc ocid1.compartment.oc1..zz -fc ocid1.compartment.oc1..zz -a XX YY
#
# Example run 3 - Dry run (no updates)
# python3 ./oci-sync-defined-tags-fss-oss.py -ad UWQV:US-ASHBURN-AD-3 -oc ocid1.compartment.oc1..zz -fc ocid1.compartment.oc1..zz -a XX YY --dryrun

##########################################################################
# Application Command line parameters
#
# usage: oci-sync-defined-tags-fss-oss.py [-h] [-pr PROFILE] [-v] [-fs FSSOCID] -fc FSSCOMPARTMENT -oc
#                                         OSSCOMPARTMENT -ad AVAILABILITYDOMAIN [--dryrun] [-ip] -a
#                                         AUTOTAG [AUTOTAG ...]
#
# options:
#   -h, --help            show this help message and exit
#   -pr PROFILE, --profile PROFILE
#                         Config Profile, named
#   -v, --verbose         increase output verbosity
#   -fs FSSOCID, --fssocid FSSOCID
#                         FSS Compartment OCID of doing a single FS
#   -fc FSSCOMPARTMENT, --fsscompartment FSSCOMPARTMENT
#                         FSS Compartment OCID
#   -oc OSSCOMPARTMENT, --osscompartment OSSCOMPARTMENT
#                         OSS Backup Comaprtment OCID
#   -ad AVAILABILITYDOMAIN, --availabilitydomain AVAILABILITYDOMAIN
#                         AD for FSS usage. Such as dDzb:US-ASHBURN-AD-1
#   --dryrun              Dry Run - print what it would do
#   -ip, --instanceprincipal
#                         Use Instance Principal Auth - negates --profile
#   -a AUTOTAG [AUTOTAG ...], --autotag AUTOTAG [AUTOTAG ...]
#                         Automatically tag backup bucket with all tags from specified namespaces.
#                         Specify like so: -a NS1 NS2
#
#
##########################################################################

import argparse
import logging
import datetime

import oci
from oci.auth.signers import InstancePrincipalsSecurityTokenSigner

#######################################
# CONSTANTS

# Define globally but set later
verbose = False

# # Set the logger
logger = logging.getLogger('oci-sync-defined-tags-fss-oss')

#######################################
# SUB ROUTINES


def ensure_backup_bucket(oss_client, bucket_name) -> bool:
    """Check bucket status - False if not there"""
    try:
        bucket = object_storage_client.get_bucket(namespace_name=namespace_name, bucket_name=bucket_name).data
        logger.info(f"Bucket {bucket_name} found")
        logger.debug(f"Bucket details: {bucket}")
    except oci.exceptions.ServiceError:
        logger.info(f"Bucket {bucket_name} not found")
        return False
    # True means we are ok to proceed
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
    #oss_defined_tags = {}
    #oss_freeform_tags = {"AUTOTAG": "DO NOT UPDATE TAGS - These are automatically synced"}
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


######################################
#  MAIN ROUTINE

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-pr", "--profile", help="Config Profile, named", default="DEFAULT")
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("--dryrun", help="Dry Run - print what it would do", action="store_true")
parser.add_argument("-fs", "--fssocid", help="FSS Compartment OCID of doing a single FS")
parser.add_argument("-fc", "--fsscompartment", help="FSS Compartment OCID", required=True)
parser.add_argument("-oc", "--osscompartment", help="OSS Backup Comaprtment OCID", required=True)
parser.add_argument("-ad", "--availabilitydomain",
                    help="AD for FSS usage.  Such as dDzb:US-ASHBURN-AD-1",
                    required=True)
parser.add_argument("-ip", "--instanceprincipal", help="Use Instance Principal Auth - negates --profile", action="store_true")
parser.add_argument("-a", "--autotag", help="Automatically tag backup bucket with all tags from specified namespaces. Specify like so:  -a NS1 NS2", nargs="+", required=True)
args = parser.parse_args()

# Process arguments
verbose = args.verbose
use_instance_principals = args.instanceprincipal
profile = args.profile
autotag_ns_list = args.autotag
dry_run = args.dryrun

# FSS Compartment OCID
fss_compartment_ocid = args.fsscompartment if args.fsscompartment else None

# FSS Single OCID
fss_ocid = args.fssocid if args.fssocid else None

# OSS Compartment OCID
oss_compartment_ocid = args.osscompartment if args.osscompartment else None

# Availability Domain
fss_avail_domain = args.availabilitydomain

# Set the log level to DEBUG or INFO
#logger = logging.getLogger(__name__)
if verbose:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

logging.info(f"Initialized Logger: {logger}")
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

# Get Object namespace
namespace_name = object_storage_client.get_namespace().data


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

# Count buckets updated
buckets_updated = 0
for share in shares.data:
    logger.info(f"Share name: {share.display_name} Size: {round(share.metered_bytes/(1024*1024*1024), 2)} GB")
    backup_bucket_name = share.display_name.strip("/") + "_backup"

    # Ensure that the bucket is there
    bucket_exists = ensure_backup_bucket(oss_client=object_storage_client,
                                         bucket_name=backup_bucket_name)

    # For for no available bucket
    if not bucket_exists:
        logger.warning(f"Bucket {backup_bucket_name} is not available for tagging {share.display_name}. Continuing.")
        continue

    # Auto-tag feature
    if autotag_ns_list and len(autotag_ns_list) > 0:
        logger.info(f"Auto-tagging bucket {backup_bucket_name} start")
        synchronize_tags(file_storage_client=file_storage_client,
                         object_storage_client=object_storage_client,
                         fs_ocid=share.id,
                         oss_namespace=namespace_name,
                         backup_bucket_name=backup_bucket_name)
        logger.info(f"Auto-tagging bucket {backup_bucket_name} complete")
        buckets_updated += 1
logger.info(f"Finished")
