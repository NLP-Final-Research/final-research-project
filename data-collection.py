import pandas as pd
import tweepy
 
# function to display data of each tweet
def printtweetdata(n, ith_tweet):
    print()
    print(f"Tweet {n}:")
    print(f"Username:{ith_tweet[0]}")
    print(f"Tweet Text:{ith_tweet[7]}")
    print(f"Hashtags Used:{ith_tweet[8]}")
 
 
# function to perform data extraction
def scrape(words, date_since, numtweet):
    db = pd.DataFrame(columns=['username', 'text', 'hashtags'])
 
    # We are using .Cursor() to search through twitter for the required tweets.
    # The number of tweets can be restricted using .items(number of tweets)
    tweets = tweepy.Cursor(api.search_tweets,
                            words, lang="en",
                           since_id=date_since,
                           tweet_mode='extended').items(numtweet)
 
    # .Cursor() returns an iterable object. Each item in the iterator has various attributes
    # that you can access to get information about each tweet
    list_tweets = [tweet for tweet in tweets]
 
    # Counter to maintain Tweet Count
    i = 1
 
    # we will iterate over each tweet in the list for extracting information about each tweet
    for tweet in list_tweets:
        username = tweet.user.screen_name
        hashtags = tweet.entities['hashtags']
        try:
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
            hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
 
    # Here we are appending all the
    # extracted information in the DataFrame
        ith_tweet = [username, text, hashtext]
        db.loc[len(db)] = ith_tweet
 
        # Function call to print tweet data on screen
        printtweetdata(i, ith_tweet)
        i = i+1
    
    filename = 'scraped_tweets.csv'
    db.to_csv(filename)

if __name__ == '__main__':
 
    # Enter your own credentials obtained from your developer account
    consumer_key = "XXXXXXXXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXX"
    access_key = "XXXXXXXXXXXXXXXXXXXXX"
    access_secret = "XXXXXXXXXXXXXXXXXXXXX"
 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
 
    # Enter Hashtag and initial date
    print("Enter Twitter HashTag to search for")
    words = input()
    print("Enter Date since The Tweets are required in yyyy-mm--dd")
    date_since = input()
 
    # number of tweets you want to extract in one run
    numtweet = 100
    scrape(words, date_since, numtweet)
    print('Scraping has completed!')