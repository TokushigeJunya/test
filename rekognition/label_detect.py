import boto3
import json
import sys
from PIL import Image

rekognition = boto3.client('rekognition')
with open(sys.argv[1], 'rb') as file:
    result = rekognition.detect_labels(Image={'Bytes': file.read()})
    print(json.dumps(result, indent=4))

image_in = Image.open(sys.argv[1])
w, h = image_in.size
for label in result['Labels']:
    if label['Instances']:
        image_out = Image.new('RGB', (w, h), (200, 200, 200))
        for instance in label['Instances']:
            box = instance['BoundingBox']
            left = int(box['Left']*w)
            top = int(box['Top']*h)
            right = left+int(box['Width']*w)
            bottom = top+int(box['Height']*h)
            image_out.paste(
                image_in.crop((left, top, right, bottom)),
                (left, top))
        name = 'label_'+label['Name']+'_'+sys.argv[1]
        print(name)
        image_out.save(name)
