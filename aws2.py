import json
import boto3
import base64
import os

s3 = boto3.cli('s3')

def bucke(data, name):
    buckname = os.environ['S3_Buck_Name']
    filedata = event['file_data']  
    filename = event['file_name']  

    # Decode the base64 file data
    filecont = base64.b64decode(filedata)

    try:
        # Upload the file to S3
        s3.put_object(Bucket=buckname, Key=filename, Body=filecont)
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully uploaded {filename} to {buckname}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }