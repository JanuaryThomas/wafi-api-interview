import boto3
import json


dynamodb = boto3.resource('dynamodb')

def handler(event, context):
    response = {"statusCode": 201, "body": "Data Added"}
    table = 'wafi-interview-dynamo-database'

    if 'body' not in event:

        response['statusCode'] = 401
        response['body'] = 'You must pass provide body'
        return response
    try:
        body = json.loads(event['body'])
        table = dynamodb.Table(table)
        table.update_item(
            Key={
                "primaryKey": body['primaryKey'],
                "secondaryKey": body['secondaryKey'],
            },
            ExpressionAttributeValues={
                ":balance": int(body['balance'])
            },
            UpdateExpression="ADD balance :balance",
            ReturnValues="UPDATED_NEW"
        )
        return response
    except Exception as e:
        print(e)
        response['statusCode'] = 505
        response['body'] = 'Could not add item'
        return