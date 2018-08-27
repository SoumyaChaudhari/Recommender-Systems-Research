
import  tweepy
import json
#TextBlob iteself gives you the sentiment polarity from -1 to 1 with -1 being negative, 0 is neutral and 1 being positive

def main():
    consumer_key = 'xsaoUwHoyqgkU4mWNl42UxzL4'
    consumer_secret = 'ckUYqvErRcZoRZQNqNlW5WrvTnrrQ57n1MAzWxyaSM0kRHxJ5w'
    access_token = '2954792182-HPM3ilDe9kaYHDWsh5a54mImcwe0VcXz8p4Vp7c'
    access_token_secret = 'QcXGLl6oUKxtStCYkbhLtjSChYoGZFhbxqLRfludbcI1s'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    retweeters = api.retweets(509457288717819904, 100)
    retweeters = convert_to_json(retweeters)
    write_to_file(retweeters)

def convert_to_json(retweets):
    result = []
    for retweet in retweets:
        if type(retweet) is tweepy.models.Status:
            result.append(retweet._json)
    return result


def write_to_file(json_data):
    with open('data.json', 'w') as outfile:
        json.dump(json_data, outfile, indent=4, sort_keys=True)

def get_retweeters_info(retweeters):
    retweeters_info = []
    for retweeter in retweeters:
        retweeters_info.append(retweeter['user'])
    return retweeters_info

"""
 TODO:
    -> Connect pymysql 
    -> Create a database and a schema to structure the information you need in tables and rows to be saved
    -> send the information to pymysql
"""

main()