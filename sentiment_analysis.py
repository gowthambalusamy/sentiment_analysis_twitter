import pandas as pd
import tweepy
import sys
from textblob import TextBlob

consumer_key = 'TbcU2f5XdsoYXjZ5TKqvC7'
consumer_secret = 'N8KgVxVcHYjbKLkWNmfUKxaqhAfY6chVWB8K48rO7T3ZJLU0HG'

access_token = '913054890-HV1FYUVkheuaYuqJPlESy4IJPo8k282RXlHfvRkt'
access_token_secret = 'Oj2Gx3d6VaBDt9xtDx9MAReyZ6XegTxK0Y7iY8bAkhf9t'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search(sys.argv[1])

textList = list()
sentimentList = list()

for tweet in public_tweets:
    txt = tweet.text
    textList.append(txt)
    analysis = TextBlob(txt)
    pol = analysis.sentiment.polarity
    print(pol)
    if(pol > 0):
        sentimentList.append('Positive')
    else:
        sentimentList.append('Negative')
    
dataFrame = pd.DataFrame({'Tweet':textList, 'Sentiment':sentimentList})
dataFrame.to_csv('sentiment.csv', sep=',', encoding='utf-8')
