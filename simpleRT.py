
import  tweepy
import json
# import pymysql
#TextBlob iteself gives you the sentiment polarity from -1 to 1 with -1 being negative, 0 is neutral and 1 being positive

def main():
    # Open database connection
    # connection = pymysql.connect(host = 'localhost',user = 'Soumya',passwd ='passwd',db ='retweets')
    # prepare a cursor object using cursor() method
    # cursor = connection.cursor()
    # execute SQL query using execute() method.
    consumer_key = 'xsaoUwHoyqgkU4mWNl42UxzL4'
    consumer_secret = 'ckUYqvErRcZoRZQNqNlW5WrvTnrrQ57n1MAzWxyaSM0kRHxJ5w'
    access_token = '2954792182-HPM3ilDe9kaYHDWsh5a54mImcwe0VcXz8p4Vp7c'
    access_token_secret = 'QcXGLl6oUKxtStCYkbhLtjSChYoGZFhbxqLRfludbcI1s'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    retweeters = api.retweets(509457288717819904, 100)
    retweeters = convert_to_json(retweeters)
    filtered_users = []
    for retweet in retweeters:
        if retweet['user']['location'] != '': 
            filtered_users.append(retweet)
    # pop_table(filtered_users)
    users_info = get_user_id(api, filtered_users)
    retweet_stat = retweet_status(api, users_info)
    write_to_file(retweet_stat)

def pop_table(filtered_users):
    arrays_of_ids = []
    arrays_of_location = []
    arrays_of_friends = []
    arrays_of_name = []
    for user in filtered_users:
        arrays_of_ids.append(user['user']['id'])
        arrays_of_name.append(user['user']['name'])
        arrays_of_location.append(user['user']['location'])
        arrays_of_friends.append(user['user']['friends_count'])
        # print('-----------')
        # print(user['user']['id'])
        # print(user['user']['name'])
        # print(user['user']['location'])
        # print(user['user']['friends_count'])
        # print('-----------')

def retweet_status(api, users):
    result = []
    for user in users:
        print('fetching users retweet....' + str(user['status']['id']))
        retweet_status = api.retweets(user['status']['id'], 100)
        print('fetched users retweet....' + str(user['status']['id']))
        print(retweet_status)
        result.append(retweet_status)
    return result

def get_user_id(api, all_users):
    users_info = []
    for user in all_users:
        try:
            print('fetching info for user with id ' + str(user['user']['id']))
            response = api.get_user(user['user']['id'])
            if type(response) is tweepy.models.User:
                users_info.append(response._json)
                print('successfully fetched user with id ' + str(user['user']['id']))
        except tweepy.error.TweepError:
            pass
    return users_info


def convert_to_json(retweets):
    result = []
    for retweet in retweets:
        if type(retweet) is tweepy.models.Status: #Specify the class to append to the array
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


main()
