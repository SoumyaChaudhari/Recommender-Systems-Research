
import  tweepy
import json
import pymysql
#TextBlob iteself gives you the sentiment polarity from -1 to 1 with -1 being negative, 0 is neutral and 1 being positive

def main():
    # Open database connection
    connection = pymysql.connect(host = 'localhost',user = 'Soumya',passwd ='passwd',db ='retweets')
    # prepare a cursor object using cursor() method
    cursor = connection.cursor()
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
    arrays_of_ids = []
    arrays_of_location = []
    arrays_of_friends = []
    arrays_of_name = []
    for user in filtered_users:
        arrays_of_ids.append(user['user']['id'])
        arrays_of_name.append(user['user']['name'])
        arrays_of_location.append(user['user']['location'])
        arrays_of_friends.append(user['user']['friends_count'])
        print('-----------')
        print(user['user']['id'])
        print(user['user']['name'])
        print(user['user']['location'])
        print(user['user']['friends_count'])
        print('-----------')
    for i in range(len(arrays_of_ids)):
        sql = ("INSERT INTO rt_info(id,name,location,friendsCount) VALUES('%d','%s','%s','%d')" % (arrays_of_ids[i],arrays_of_name[i],arrays_of_location[i],arrays_of_friends[i]))
        cursor.execute(sql)
        connection.commit()
        # Fetch a single row using fetchone() method.
    data = cursor.fetchall()

    write_to_file(filtered_users)

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

"""
 TODO:
    -> Connect pymysql 
    -> Create a database and a schema to structure the information you need in tables and rows to be saved
    -> send the information to pymysql
"""

main()