import boto3
import json
import sys
from PIL import Image

rekognition = boto3.client('rekognition')
collection_id = 'MyCollection'

with open(sys.argv[1], 'rb') as file:
    result = rekognition.search_faces_by_image(
        CollectionId=collection_id,
        Image={'Bytes': file.read()})
    print(json.dumps(result, indent=4))

image_in = Image.open(sys.argv[1])
w, h = image_in.size
image_out = Image.new('RGB', (w, h), (200, 200, 200))
if result['FaceMatches']:
    box = result['SearchedFaceBoundingBox']
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)
    image_out.paste(
        image_in.crop((left, top, right, bottom)),
        (left, top))
image_out.save('search_'+sys.argv[1])
image_out.show()
