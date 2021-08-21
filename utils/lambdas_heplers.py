from datetime import datetime
from decimal import Decimal
import functools

def dynamo_parser(obj: dict) -> dict:
    if isinstance(obj, Decimal):
        return str(obj)
    if isinstance(obj, datetime):
        return str(obj)

def response() -> dict:

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "*",
        },
        "body": "200-OK",
    }

def api(func):
    pass