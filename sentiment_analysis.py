import boto3
import json

# Once the sentiment for the conversation reaches a certain negative limit, we can alert social workers who can take human action

comprehend = boto3.client(service_name='comprehend', region_name='ap-southeast-1')

f = open("src/response.txt", "r")
text = f.read()

print(comprehend.detect_sentiment(Text=text, LanguageCode='en')['Sentiment'])

positive = comprehend.detect_sentiment(Text=text, LanguageCode='en')['SentimentScore']['Positive']
negative = comprehend.detect_sentiment(Text=text, LanguageCode='en')['SentimentScore']['Negative']
print(f"It is {positive*100:.2f}% positive and {negative*100:.2f}% negative")