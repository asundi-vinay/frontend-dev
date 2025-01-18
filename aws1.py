import json

def add_num(number,sum):
    n1=number.get('n1')
    n2=number.get('n2')
    result=n1+n2
    return{
        'statusCode':200,
        'body':json.dumps({'res':result})
        
    }


