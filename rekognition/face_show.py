import boto3
import json
import sys
from PIL import Image

rekognition = boto3.client('rekognition')
with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_faces(
        Image={'Bytes': file.read()})
    print(json.dumps(result, indent=4))

image_in = Image.open(sys.argv[1])
w, h = image_in.size
image_out = Image.new('RGB', (w, h), (200, 200, 200))
for face in result['FaceDetails']:
    box = face['BoundingBox']
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)
    image_out.paste(
        image_in.crop((left, top, right, bottom)),
        (left, top))
image_out.save('show_'+sys.argv[1])
image_out.show()
