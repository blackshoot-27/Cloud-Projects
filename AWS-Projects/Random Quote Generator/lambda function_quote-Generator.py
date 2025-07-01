import json
import urllib.request

def lambda_handler(event, context):
    url = "https://zenquotes.io/api/random"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            html_quote = data[0].get('h', '<p>No quote found</p>')

            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Content-Type': 'application/json'
                },
                'body': json.dumps({'quote_html': html_quote})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
