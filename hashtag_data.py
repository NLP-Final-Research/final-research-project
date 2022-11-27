# Importing the libraries
import configparser
import tweepy
import csv

# Read the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Read the values
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

csvFile = open('tweets.csv', 'w')
csvWriter = csv.writer(csvFile)

hashtag = "#supporttrump"
date_since = "2022-02-01"
limit=2


for tweet in tweepy.Cursor(api.search_tweets, hashtag, lang="en", since_id=date_since, tweet_mode='extended').items(limit):
  # print(tweet.full_text)
  csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

csvFile.close()
