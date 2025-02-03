import json
import boto3
import os
import uuid

# Initialize DynamoDB
dynamodb = boto3.resource("dynamodb")
table_name = os.environ["DYNAMODB_TABLE"]
table = dynamodb.Table(table_name)

# Lambda function to handle requests
def lambda_handler(event, context):
    body = json.loads(event["body"])
    user_id = str(uuid.uuid4())  # Generate unique ID

    item = {
        "userId": user_id,
        "name": body["name"],
        "email": body["email"]
    }

    # Store in DynamoDB
    table.put_item(Item=item)

    return {
        "statusCode": 201,
        "body": json.dumps({"message": "User created!", "userId": user_id})
    }
