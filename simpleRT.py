
import  tweepy
import json
#TextBlob iteself gives you the sentiment polarity from -1 to 1 with -1 being negative, 0 is neutral and 1 being positive

consumer_key = 'xsaoUwHoyqgkU4mWNl42UxzL4'
consumer_secret = 'ckUYqvErRcZoRZQNqNlW5WrvTnrrQ57n1MAzWxyaSM0kRHxJ5w'
access_token = '2954792182-HPM3ilDe9kaYHDWsh5a54mImcwe0VcXz8p4Vp7c'
access_token_secret = 'QcXGLl6oUKxtStCYkbhLtjSChYoGZFhbxqLRfludbcI1s'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

response = api.retweets(509457288717819904, 100)

print(response)

