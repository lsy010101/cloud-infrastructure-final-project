import boto3
import json
 
dynamodb = boto3.client('dynamodb')
TABLE_NAME = 'Inventory'
 
def lambda_handler(event, context):
    if 'pathParameters' not in event or 'id' not in event['pathParameters'] or 'location_id' not in event['pathParameters']:
        return {
            'statusCode': 400,
            'body': json.dumps("Missing 'id' or 'location_id' path parameter")
        }
 
    key = {
        'id': { 'S': event['pathParameters']['id'] },
        'location_id': { 'N': event['pathParameters']['location_id'] }
    }
 
    try:
        response = dynamodb.get_item(TableName=TABLE_NAME, Key=key)
        item = response.get('Item', {})
 
        if not item:
            return {
                'statusCode': 404,
                'body': json.dumps('Item not found')
            }
 
        return {
            'statusCode': 200,
            'body': json.dumps(item, default=str)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }