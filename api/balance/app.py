import boto3
import json
from decimal import Decimal


dynamodb = boto3.resource('dynamodb')
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)

def handler(event, context):
    response = {"statusCode": 201, "body": "Data Added"}
    table = 'wafi-interview-dynamo-database'

    if 'body' not in event:

        response['statusCode'] = 401
        response['body'] = 'You must pass provide body'
        return response
    try:
        pathParameters = event["pathParameters"]
        table = dynamodb.Table(table)
        item = table.get_item(
            Key={
                "primaryKey": pathParameters['primaryKey'],
                "secondaryKey": pathParameters['secondaryKey'],
            }
        )
        response['body'] = json.dumps(item['Item'], cls=DecimalEncoder)
        return response
    except Exception as e:
        print(e)
        response['statusCode'] = 505
        response['body'] = 'Could not add item'
        return