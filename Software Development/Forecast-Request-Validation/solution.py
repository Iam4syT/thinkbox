import json
import math

def handler(event, context=None):
    try:
        reading = json.loads(event['body'])['irradiance']
    except (KeyError, TypeError, ValueError):
        return {'statusCode': 400, 'body': 'Invalid input'}
    if type(reading) not in (float, int) or not math.isfinite(reading) or reading < 0:
        return {'statusCode': 400, 'body': 'Invalid reading'}
    return {'statusCode': 200, 'body': json.dumps({'accepted': reading})}
