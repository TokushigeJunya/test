import boto3
import json
import sys

rekognition = boto3.client('rekognition')
collection_id = 'MyCollection'

print('create_collection:')
result = rekognition.create_collection(CollectionId=collection_id)
print(json.dumps(result, indent=4))

print('index_faces:')
for path in sys.argv[1:]:
    with open(path, 'rb') as file:
        result = rekognition.index_faces(
            CollectionId=collection_id,
            Image={'Bytes': file.read()})
        print(json.dumps(result, indent=4))

print('list_collections:')
result = rekognition.list_collections()
print(json.dumps(result, indent=4))

print('list_faces:')
result = rekognition.list_faces(CollectionId=collection_id)
print(json.dumps(result, indent=4))
