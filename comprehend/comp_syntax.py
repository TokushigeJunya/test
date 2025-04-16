import boto3
comprehend = boto3.client('comprehend', 'us-east-2')
text = "I'm looking forward to visiting Japan next summer."
result = comprehend.detect_syntax(Text=text, LanguageCode='en')
for token in result['SyntaxTokens']:
    print('{:20} {:20} {:<018}'.format(
        token['Text'],
        token['PartOfSpeech']['Tag'],
        token['PartOfSpeech']['Score']))
