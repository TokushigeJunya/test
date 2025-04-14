import boto3
import json
rekognition = boto3.client('rekognition')
collection_id = 'MyCollection'
result = rekognition.delete_collection(CollectionId=collection_id)
print(json.dumps(result, indent=4))
