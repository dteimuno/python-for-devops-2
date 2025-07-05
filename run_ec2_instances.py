import boto3

client = boto3.client("ec2")

def create_ec2_instance(image_id, instance_type, count):
    """
    Launch one or more EC2 instances with the given parameters.
    """
    response = client.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        KeyName="keypairforluitccp3",
        MinCount=count,
        MaxCount=count,
        Monitoring={"Enabled": True},
        SecurityGroupIds=["<put-your-here>"],
        SubnetId="<put-yours-here>",
        TagSpecifications=[
            {
                "ResourceType": "instance",       
                "Tags": [
                    {"Key": "environment", "Value": "development"},
                ],
            }
        ],
    )

    return response


if __name__ == "__main__":
    create_ec2_instance("ami-020cba7c55df1f615", "t2.micro", 1)
