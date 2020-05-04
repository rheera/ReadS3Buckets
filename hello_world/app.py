import json
import boto3

# sets up an S3 service object we can interface with (call methods on and work with)
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    # make an empty list
    bucket_list = []
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
