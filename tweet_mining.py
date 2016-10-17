import tweepy
import time
import sys
import csv
import pandas as pd


#get keys and tokens from https://apps.twitter.com/
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

#use keys and tokens to create tweepy api object
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


#create a list of 50 tweets that have #kenbone in text
results = []
for tweet in tweepy.Cursor(api.search, q = "#kenbone").items(50):
    results.append(tweet)
print(len(results))


#create dataframe to display specific parts of tweet 
#https://gist.github.com/hrp/900964  --example api request
#use ^^^ link to find keys in json file to search then use "tweet." classes to find the one that matches the key
def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])
    #tweet data
    data_set["text"] = [tweet.text for tweet in results]
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["source"] = [tweet.source for tweet in results]
    
    
    #user data
    data_set["user_id"] = [tweet.author.id for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_name"] = [tweet.author.name for tweet in results]
    data_set["user_description"] = [tweet.author.description for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]
    data_set["lang"] = [tweet.author.lang for tweet in results]
    
    return data_set
data_set= process_results(results)


#show first 20 rows of dataframe
data_set.head(20)


#dataframe to csv
data_set.to_csv('kenbone_tweets.csv')
