import boto3
comprehend = boto3.client('comprehend', 'us-east-2')
with open('comp_phrase.txt', 'r', encoding='utf-8') as file:
    result = comprehend.detect_key_phrases(
        Text=file.read(), LanguageCode='en')
    report = {}
    for phrase in result['KeyPhrases']:
        text, score = phrase['Text'], phrase['Score']
        report[text] = '{:<018} {}'.format(score, text)
    for line in sorted(report.values(), reverse=True):
        print(line)
