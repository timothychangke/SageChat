import boto3
import json
import spacy

# Once the sentiment for the conversation reaches a certain negative limit, we can alert social workers who can take human action

comprehend = boto3.client(service_name='comprehend', region_name='ap-southeast-1')

f = open("src/response.txt", "r")
text = f.read()

print(comprehend.detect_sentiment(Text=text, LanguageCode='en')['Sentiment'])

positive = comprehend.detect_sentiment(Text=text, LanguageCode='en')['SentimentScore']['Positive']
negative = comprehend.detect_sentiment(Text=text, LanguageCode='en')['SentimentScore']['Negative']
print(f"It is {positive*100:.2f}% positive and {negative*100:.2f}% negative")


"""
We can also extract some medical data that could be in the conversation
Would be able to extract out medical information such as drugs, dosage, duration and other relevant information such that
it can provide succinct information to social workers or doctors so that they can take this into consideration to decide whether to 
intervene and take human action.
The model would analyze the conversation line by line and only extract out medical information.
"""

med7 = spacy.load("en_core_med7_lg")

with open('src/response.txt', 'r') as f:
    last_line = f.readlines()[-1]

text = last_line
doc = med7(text)
print("\n")
for ent in doc.ents:
    print(ent.text, ent.label_)