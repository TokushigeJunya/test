import boto3
import csv
import json
comprehend = boto3.client('comprehend', 'us-east-2')
with open('comp_language.csv', 'r', encoding='utf-8') as file:
    for row in csv.reader(file):
        result = comprehend.detect_dominant_language(Text=row[2])
        print(row[2])
        for language in result['Languages']:
            print(language['LanguageCode'], language['Score'])
        print()
