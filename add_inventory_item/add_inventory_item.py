import boto3
import json
import uuid
from decimal import Decimal
 
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Inventory')
 
def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
 
        new_id = str(uuid.uuid4())
 
        item = {
            'id': new_id,
            'location_id': Decimal(str(data['location_id'])),
            'name': data['name'],
            'description': data['description'],
            'qty': Decimal(str(data['qty'])),
            'price': Decimal(str(data['price']))
        }
 
        table.put_item(Item=item)
 
        return {
            'statusCode': 200,
            'body': json.dumps(f"Item {new_id} added.")
        }
 
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }