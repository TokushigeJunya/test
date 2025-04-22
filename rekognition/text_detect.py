import boto3
import json
import sys
from PIL import Image

if len(sys.argv) != 2:
    print('python', sys.argv[0], 'image')
    exit()

rekognition = boto3.client('rekognition')
with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_text(Image={'Bytes': file.read()})
    print(json.dumps(result, indent=4))

image_in = Image.open(sys.argv[1])
w, h = image_in.size
for text in result['TextDetections']:
    image_out = Image.new('RGB', (w, h), (200, 200, 200))
    box = text['Geometry']['BoundingBox']
    left = int(box['Left']*w)
    top = int(box['Top']*h)
    right = left+int(box['Width']*w)
    bottom = top+int(box['Height']*h)
    image_out.paste(
        image_in.crop((left, top, right, bottom)), (left, top))
    name = text['Type']+'_'+text['DetectedText']+'_'+sys.argv[1]
    print(name)
    image_out.save(name)
