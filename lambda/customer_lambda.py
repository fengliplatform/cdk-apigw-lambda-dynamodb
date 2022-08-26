import json
import os
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    data = json.loads(event["body"])

    dynamodb = boto3.resource('dynamodb')
    TABLE_NAME = os.environ['TABLE_NAME']
    table = dynamodb.Table(TABLE_NAME)
    
    table.put_item(Item={
                "customer_id": data["customer_id"],
                "name": data["name"],
                "email": data["email"]
            }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('User Added!')
    }