import boto3

client = boto3.client("s3", region_name="us-east-1")   

def create_s3_bucket():
    """
    Create a private S3 bucket named dtm-python-devops2.
    """
    client.create_bucket(
        Bucket="dtm-python-devops2",
        ACL="private"

    )

if __name__ == "__main__":
    create_s3_bucket()

