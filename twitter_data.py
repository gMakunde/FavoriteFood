import requests, requests_oauthlib
import random
import os
import fmt

class TwitterData:
    """
A class used to get twitter json

...

Attributes
----------
url: str
a string containing a twitter api endpoint
key: str
twitter-dev api key
secret_key: str
twitter-dev api secret key
token: str
twitter-dev access token
secret_token: str
twitter-dev token secret

Methods
--------
get_json()
returns json body of the endpoint
get_random_tweets(twit_json_body)
returns a list containing 5 random tweets from the twit_json_body
"""
    def __init__(self):
        """
Parameters
----------
url: str
a string containing a twitter api endpoint
key: str
twitter-dev api key
secret_key: str
twitter-dev api secret key
token: str
twitter-dev access token
secret_token: str
twitter-dev token secret
"""
        self.url = "https://api.twitter.com/1.1/search/tweets.json?q=falafel%20hummus&result_type=mixed"
        self.key = os.getenv('twit_key')
        self.secret_key = os.getenv('twit_secret')
        self.token = os.getenv('twit_token')
        self.secret_token = os.getenv('twit_token_secret')
    
    def get_json(self):
        """returns json body of the endpoint

Returns
--------
json
json body of twitter endpoint
"""
        twit_oauth = requests_oauthlib.OAuth1(
            self.key,
            self.secret_key,
            self.token,
            self.secret_token,
        )
        print(fmt.Println(twit_oauth))
        print("key: " + self.key)
        print("secret key: " + self.secret_key)
        print("token: " + self.token)
        print("token secret: " + self.secret_token)
        rad= """Response
        ========================================================================"""
        print(rad)
        print(requests.get(self.url, auth=twit_oauth).json())
        return requests.get(self.url, auth=twit_oauth).json()
        
    def get_random_tweets(self, twit_json_body):
        """returns a list containing 5 random tweets from the twit_json_body

Parameters
----------
twit_json_body: json
the json body from a twitter endpoint

Returns
--------
list
list of 5 random tweet ids
"""
        twit_random = random.randint(0, len(twit_json_body["statuses"])-5)
        tweets = []
        for i in range(5):
            tweets.append(twit_json_body["statuses"][twit_random+i]['id'])
        return tweets
        
