try:
    import boto3
    import os
except ImportError:
    print("Cannot import modules")
    raise

def listBuckets(client):
    args = {}
    buckets = []
    try:
        while True:
            response = client.list_buckets(**args)
            if response:
                if response.get('Buckets', []):
                    for bucket in response['Buckets']:
                        buckets.append(bucket['Name'])
            if 'NextToken' in response:
                args['NextToken'] = response['NextToken']
            else:
                break
        return buckets
    except Exception as e:
        print('Unable to list buckets with error: {}'.format(str(e)))
        return []
     
if __name__ == 'main':
    region = 'eu-west-1'
    s3Client = boto3.client('s3', region_name=region)
    buckets = listBuckets(client=s3Client)
    print('Buckets on account: {}'.format(buckets))

