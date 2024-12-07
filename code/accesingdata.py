# This work was realized as part of the capstone project of the MS in Data Science at Pace University by Lolyna de la Fuente Ordaz
# Libraries and Dependencies
import boto3
from botocore.exceptions import NoCredentialsError
import os

# Setting up Authentication and Endpoint
# API ACCESS KEY ID AND API SECRET ACCESS KEY will be created under your SourceCoop Account
aws_access_key_id = '<YOUR_API_ACCESS_KEY_ID_HERE>'
aws_secret_access_key = '<YOUR_API_SECRET_ACCESS_KEY_HERE>'
endpoint_url = 'https://data.source.coop'
bucket_name = 'nasa'
prefix = 'tropical-storm-competition/'
local_directory = '.'  # Local directory to sync to
last_downloaded_file = 'last_downloaded.txt'  # File to track the last downloaded file

# Defining allowed document extensions
doc_extensions = ['.jpg', '.csv']

# Creating an S3 client with custom endpoint
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    endpoint_url=endpoint_url,
)

def get_last_downloaded_file():
    """Read the last downloaded file from the last_downloaded.txt"""
    if os.path.exists(last_downloaded_file):
        with open(last_downloaded_file, 'r') as f:
            return f.read().strip()
    return None

def update_last_downloaded_file(file_key):
    """Update the last downloaded file in last_downloaded.txt"""
    with open(last_downloaded_file, 'w') as f:
        f.write(file_key)

def download_s3_folder(bucket_name, prefix, local_dir):
    """
    Download only non-existing image files from a folder in an S3 bucket, starting from the last downloaded file.
    bucket_name: The name of the S3 bucket
    prefix: The folder prefix in the S3 bucket
    local_dir: The local directory to store the downloaded files
    """
    # Use ListObjectsV2 to get the objects under the prefix
    paginator = s3_client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    last_downloaded = get_last_downloaded_file()  # Get the last downloaded file from the file

    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                target = os.path.join(local_dir, obj['Key'][len(prefix):])

                # Skip files that already exist or have been downloaded
                if os.path.exists(target):
                    print(f"File {target} already exists, skipping download.")
                    continue

                # Skip files that are not images based on their extensions
                if not any(obj['Key'].lower().endswith(ext) for ext in doc_extensions):
                    print(f"Skipping non-doc allowed extension file {obj['Key']}")
                    continue

                # If the last downloaded file is set and it's passed, skip until we reach the last downloaded file
                if last_downloaded and obj['Key'] <= last_downloaded:
                    print(f"Skipping {obj['Key']} (already downloaded)")
                    continue

                # If the object is a folder, create it locally
                if not os.path.exists(os.path.dirname(target)):
                    os.makedirs(os.path.dirname(target))

                # Download the file from the S3 bucket to the local directory
                print(f"Downloading {obj['Key']} to {target}")
                try:
                    s3_client.download_file(bucket_name, obj['Key'], target)
                    update_last_downloaded_file(obj['Key'])  # Update last downloaded file
                except Exception as e:
                    print(f"Error downloading {obj['Key']}: {e}")

if __name__ == "__main__":
    download_s3_folder(bucket_name, prefix, local_directory)
