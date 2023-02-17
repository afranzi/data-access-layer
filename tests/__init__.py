import json

import boto3

AWS_REGION = "us-east-1"


def set_up_secret(secret_name, content: dict):
    conn = boto3.client("secretsmanager", region_name=AWS_REGION)
    conn.create_secret(Name=secret_name, SecretString=json.dumps(content))
