import boto3
comprehend = boto3.client('comprehend', 'us-east-2')
text = "I'm looking forward to visiting Japan next summer."
result = comprehend.detect_entities(Text=text, LanguageCode='en')
for entity in result['Entities']:
    print('{:20} {:20} {:<018}'.format(
        entity['Text'], entity['Type'], entity['Score']))
