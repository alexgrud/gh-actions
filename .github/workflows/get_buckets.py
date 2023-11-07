try:
    import boto3
    import os
except ImportError:
    print("Cannot import modules")
    raise

if __name__ == 'main':
    region = 'eu-west-1'
    client = boto3.client('s3', region_name=region)

