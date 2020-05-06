import boto3

# sets up an S3 service object we can interface with (call methods on and work with)
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    # make an empty list
    bucket_list = []
    # for loop to print the bucket names and add them to our list
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket_list.append(bucket.name)
    return {
        "statusCode": 200,
        "body": bucket_list,
    }
