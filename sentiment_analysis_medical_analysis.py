import boto3
import json
import spacy
import pandas as pd
import numpy as np
from tqdm import tqdm
import seaborn as sns

"""
Once the sentiment for the conversation reaches a certain negative limit, we can alert social workers who can take human action
"""

comprehend = boto3.client(service_name='comprehend', region_name='ap-southeast-1')

sentiment_df = pd.DataFrame()
positive_arr = []
negative_arr = []

for i in tqdm(range(7)):
    f = open(f"responses/responses_{i+1}.txt", "r")
    text = f.read()
    # print(comprehend.detect_sentiment(Text=text, LanguageCode='en')['Sentiment'])
    positive = comprehend.detect_sentiment(Text=text, LanguageCode='en')['SentimentScore']['Positive']
    negative = comprehend.detect_sentiment(Text=text, LanguageCode='en')['SentimentScore']['Negative']
    # print(f"It is {positive*100:.2f}% positive and {negative*100:.2f}% negative")
    positive_arr.append(positive*100)
    negative_arr.append(negative*100)

sentiment_df['Positive'] = positive_arr
sentiment_df['Negative']=negative_arr
print(sentiment_df)

plot = sns.histplot(data = sentiment_df, x = sentiment_df['Negative'])
fig = plot.get_figure()
fig.savefig("out.png") 

"""
We can also extract some medical data that could be in the conversation
Would be able to extract out medical information such as drugs, dosage, duration and other relevant information such that
it can provide succinct information to social workers or doctors so that they can take this into consideration to decide whether to 
intervene and take human action.
The model would analyze the conversation line by line and only extract out medical information.
"""

med7 = spacy.load("en_core_med7_lg")
data_collected = []

for i in tqdm(range(7)):
    with open(f"responses/responses_{i+1}.txt", "r") as f:
        last_line = f.readlines()[-1]
    text = last_line
    doc = med7(text)
    for ent in doc.ents:
        if len(ent.text) != 0:
            print(ent.text, ent.label_)
            data_collected.append((ent.text, ent.label_))

print(data_collected)


# Deploying with streamlit 