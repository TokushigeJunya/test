import boto3
import csv
region = 'us-east-2'
translate = boto3.client('translate', region)
comprehend = boto3.client('comprehend', region)
with open('comp_sentiment.csv', 'r', encoding='utf-8') as file:
    for row in csv.reader(file):
        result_en = translate.translate_text(
            Text=row[2],
            SourceLanguageCode='auto',
            TargetLanguageCode='en')
        result_ja = translate.translate_text(
            Text=row[2],
            SourceLanguageCode='auto',
            TargetLanguageCode='ja')
        result_comp = comprehend.detect_sentiment(
            Text=result_en['TranslatedText'],
            LanguageCode='en')
        print(row[2])
        print('(', result_en['TranslatedText'], ')')
        print('(', result_ja['TranslatedText'], ')')
        print(result_comp['Sentiment'])
        for key, value in result_comp['SentimentScore'].items():
            print('  {:10} {}'.format(key, value))
        print()
