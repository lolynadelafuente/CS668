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

# Creating an S3 client with custom endpoint
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    endpoint_url=endpoint_url,
)

# Creating an S3 resource
s3_resource = boto3.resource(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    endpoint_url=endpoint_url,
)

# Downloading Function
def download_s3_folder(bucket_name, prefix, local_dir):
    """
    Downloading the contents of a folder from an S3 bucket
    bucket_name: The name of the S3 bucket
    prefix: The folder prefix in the S3 bucket
    local_dir: The local directory to store the downloaded files
    """
    bucket = s3_resource.Bucket(bucket_name)

    # Using ListObjectsV2 to get the objects under the folder prefix
    paginator = s3_client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                target = os.path.join(local_dir, obj['Key'][len(prefix):])
                
                # If the object is a folder, create it locally
                if not os.path.exists(os.path.dirname(target)):
                    os.makedirs(os.path.dirname(target))

                # Download the file from the S3 bucket to the local directory
                print(f"Downloading {obj['Key']} to {target}")
                try:
                    s3_client.download_file(bucket_name, obj['Key'], target)
                except NoCredentialsError:
                    print("Credentials not available. Please check your AWS access keys.")
                    break

if __name__ == "__main__":
    download_s3_folder(bucket_name, prefix, local_directory)
