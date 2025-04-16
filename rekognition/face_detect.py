import boto3
import json
import sys

rekognition = boto3.client('rekognition')
with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_faces(Image={'Bytes': file.read()})
    print(json.dumps(result, indent=4))
