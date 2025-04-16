import boto3
import json
comprehend = boto3.client('comprehend', 'us-east-2')
text = "I'm looking forward to visiting Japan next summer."
result = comprehend.detect_dominant_language(Text=text)
print(json.dumps(result, indent=4))
