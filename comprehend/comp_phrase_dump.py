import boto3
import json
comprehend = boto3.client('comprehend', 'us-east-2')
text = "I tried to use the 20% OFF coupon, \
but only 10% discount and I was unable to place an order."
result = comprehend.detect_key_phrases(Text=text, LanguageCode='en')
print(json.dumps(result, indent=4))
