import logging
import boto3
from botocore.exceptions import ClientError
import os

#s3 = boto3.resource("s3")
#for bucket in s3.buckets.all():
#    print(bucket.name)
#########################################

# Read inputs #
file_name,bucket,object_name=input("").split(",")

def upload_file(file_name,bucket,object_name=None):
    if object_name is None:
        object_name = os.path.basename(file_name)
    #create obj
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name,bucket,object_name)
    except ClientError as e:
            logging.error(e)
            return False
    return True

#open file as binary
open(file_name, "rb")
#calling the function
upload_file(file_name,bucket,object_name)
