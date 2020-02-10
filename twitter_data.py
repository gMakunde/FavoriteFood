import requests, requests_oauthlib
import random
import os

class TwitterData:
    """
    A class used to get twitter json.
    
    Attributes:
        url (str): A string containing a twitter api endpoint.
        key (str): A twitter-dev api key.
        secret_key (str): A twitter-dev api secret key.
        token (str): A twitter-dev access token.
        secret_token (str): A twitter-dev token secret.
    """
    def __init__(self):
        """
        The constructor for the TwitterData class.
        """
        self.url = "https://api.twitter.com/1.1/search/tweets.json?q=falafel%20hummus&result_type=mixed"
        self.key = os.getenv('twit_key')
        self.secret_key = os.getenv('twit_secret')
        self.token = os.getenv('twit_token')
        self.secret_token = os.getenv('twit_token_secret')
    
    def get_json(self):
        """
        A method that returns the json body of the endpoint.

        Returns:
            dict: The json body of the twitter endpoint.
        """
        twit_oauth = requests_oauthlib.OAuth1(
            self.key,
            self.secret_key,
            self.token,
            self.secret_token,
        )
        
        return requests.get(self.url, auth=twit_oauth).json()
        
    def get_random_tweets(self, twit_json_body):
        """
        A method that returns a list containing 5 random tweets from the 
        twit_json_body.

        Parameters:
            twit_json_body (dict): The json body from a twitter endpoint.
        
        Returns:
            list: A list that contains 5 random tweet ids from twit_json_body.
        """
        twit_random = random.randint(0, len(twit_json_body["statuses"])-5)
        tweets = []
        for i in range(5):
            tweets.append(twit_json_body["statuses"][twit_random+i]['id'])
        return tweets
        
