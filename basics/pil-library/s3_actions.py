import boto3
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='karthick-learner')
s3_client = session.client('s3')

bucket_name = 'karthick-leaner-ccp-2021-demo'
res = s3_client.list_objects(Bucket=bucket_name)
# print(res)
contents = res.get('Contents')
# print(contents)
for content in contents:
    key = content.get('Key')
    print(key)
