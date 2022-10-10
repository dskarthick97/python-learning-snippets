
import boto3
import uuid
from PIL import Image
from urllib.parse import unquote_plus
from botocore.exceptions import ClientError

# session = boto3.Session(profile_name='karthick-learner')
s3_client = session.client('s3')


class ThumbnailGenerator(object):

    def __init__(self, event):
        self.event = event

    @staticmethod
    def resize_image(image_path, resized_path):
        with Image.open(image_path) as image:
            image.thumbnail(tuple(x / 2 for x in image.size))
            image.save(resized_path)

    def generate_thumbnail(self):
        for record in self.event['Records']:
            bucket = record['s3']['bucket']['name']
            key = unquote_plus(record['s3']['object']['key'])
            tmpkey = key.replace('/', '')

            download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
            upload_path = '/tmp/resized-{}'.format(tmpkey)

            s3_client.download_file(bucket, key, download_path)
            self.resize_image(download_path, upload_path)
            s3_client.upload_file(upload_path, 'demo-thumbnail-generation-bucket', key)

        return {
            200,
            f'Successfully generated'
        }


def lambda_handler(event, context=None):
    try:
        response = ThumbnailGenerator(event).generate_thumbnail()
        print(response)
    except ClientError as error:
        print(error)

if __name__ == '__main__':
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "karthick-leaner-ccp-2021-demo"
                    },
                    "object": {
                        "key": "private/up/up-balloon-home.jpg"
                    }
                }
            }
        ]
    }
    lambda_handler(event)
