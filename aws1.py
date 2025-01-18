import json
def add_num(number, sum):
    try:
        n1 = number.get('n1', 0)
        n2 = number.get('n2', 0)
        result = n1 + n2
        return {
            'statusCode': 200,
            'body': json.dumps({'result': result})
        }
    except TypeError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid input'})
        }


