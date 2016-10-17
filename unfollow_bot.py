import sys
import time
import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#create a list of followers
followers = []
for follower in tweepy.Cursor(api.followers_ids).items(5):
    followers.append(follower)
print ("Found %s followers, finding friends.." % len(followers))


#create a list of your friends
friends = []
for friend in tweepy.Cursor(api.friends_ids).items(5):
    friends.append(friend)
#for every person you follow that doesn't follow you back, remove them
for friend in friends:
    if friend not in followers:
        print ("Unfollow {0}?".format(api.get_user(friend).screen_name))
        if input("Y/N?") == 'y' or 'Y':
            api.destroy_friendship(friend)