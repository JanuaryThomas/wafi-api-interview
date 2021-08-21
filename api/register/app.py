import boto3
import json
def addItem(table, item) -> bool:
        """[summary]
        Returns:
            bool: [description]
        """

        dynamodb = boto3.resource("dynamodb")

        table = dynamodb.Table(table)
        try:
            table.put_item(Item=item)
            return True
        except Exception as e:
            print(e)
            return False


def handler(event: dict, context: dict):

    response = {"statusCode": 201, "body": "Data Added"}
    table = 'wafi-interview-dynamo-database'

    if 'body' not in event:

        response['statusCode'] = 401
        response['body'] = 'You must pass provide body'
        return response
    
    body = json.loads(event['body'])
    if addItem(table, body):
        return response
    response['statusCode'] = 505
    response['body'] = 'Could not add item'
    return response