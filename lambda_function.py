import json

def hello(event, context):
    try:
        # Get the query parameter 'name' from the event
        name = event.get('queryStringParameters', {}).get('name', 'World')
# new comment
        # Generate the greeting message
        message = f"Hello, {name}!"

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({'message': message})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }