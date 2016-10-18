import sys
import time
import tweepy
import pandas as pd

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

tweet_ids = []       #holds twitter ids to later compare to list of our friends ids
tweet_text = []       #holds entire tweet json response for each user
for tweet in tweepy.Cursor(api.search, q='#kenbone').items(100): 
    tweet_ids.append(tweet.author.id)
    tweet_text.append(tweet)
    

friends_id = []       #create a list containing twitter ids of people who follow you--aka friends
for friend in tweepy.Cursor(api.friends_ids).items(100):
    friends_id.append(friend)


def process_results(): #create a function to index specific parts of each tweet and store in dataframe 
    first_column = [tweet.author.screen_name for tweet in tweet_text]
    data_set = pd.DataFrame(first_column, columns = ["@ User Name"])
    data_set["# of Followers"] = [tweet.author.followers_count for tweet in tweet_text]
    data_set["Tweet Text"] = [tweet.text for tweet in tweet_text]
    data_set["User location"] = [tweet.author.location for tweet in tweet_text]
    data_set["Retweet Count"] = [tweet.retweet_count for tweet in tweet_text]
    data_set["User Description"] = [tweet.author.description for tweet in tweet_text]
    return data_set

df= process_results()           #store function into variable so its easier to call later

for tweet in tweet_user:       #for each tweet in our search
    if tweet not in friends_id:               #if we don't already follow the author
        for i, tweet in enumerate(tweet_ids): #'make indexable' twitter ids
            var = df.ix[i]                     #store indexes of df variable into another variable
            print("{}%".format(var), '\n')     #print [0] from df only, we only need to match order of tweet_ids with df...
            print ("Follow {0}?".format(api.get_user(tweet).screen_name)) #...which is then matched with the tweeters screen name
            if input("Y/N?") == 'y' or 'Y':
                api.create_friendship(tweet)
            print ('\n\n')