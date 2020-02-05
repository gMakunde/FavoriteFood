import flask
import os
import random
import requests, requests_oauthlib
import json
import os
import random

app = flask.Flask(__name__)


@app.route('/')
def index():
    
    twit_url = "https://api.twitter.com/1.1/search/tweets.json?q=sabich&result_type=mixed"
    #twit_key = os.getenv('Twitter_Key')
    # twit_secret = os.getenv('Twitter_Secret')
    # twit_token = os.getenv('Twitter_Token')
    # twit_token_secret = os.getenv('Twitter_Token_Secret')
    # twit_oauth = requests_oauthlib.OAuth1(
    #     twit_key,
    #     twit_secret,
    #     twit_token,
    #     twit_token_secret,
    # )
    
    twit_oauth = requests_oauthlib.OAuth1(
        "KJFYSqLhZ8rwQiXJsvkjN9GzF",
        "J7G5iZndpRmiH5tzihuJxHQe0nDYpxvVhQ1W4v9OOpQrujurXn",
        "519031926-OmiqDkHu7pIaLSZqRknbD5fp9uwFF9m4ah2ZPypC",
        "HOcM2UpzwoVVlxTmD1tihORc9hWGcJatOW1cK1Z6GaVMv",
    )
    twit_response = requests.get(twit_url, auth=twit_oauth)
    twit_json_body = twit_response.json()
    twit_random = random.randint(0, len(twit_json_body["statuses"])-5)
    spoonacular_url = "https://api.spoonacular.com/recipes/informationBulk?ids=763234,602727,200239"
    #spoonacular_key = os.getenv('spoonKey')
    spoonacular_key = "&apiKey=0df474a2434e4aefacf96e34ba4a7761"
    spoonacular_response = requests.get(spoonacular_url + spoonacular_key)
    spoonacular_json_body = spoonacular_response.json()
    random_recipie = random.randint(0, len(spoonacular_json_body)-1)
    
    print(twit_json_body)
    tweets = []
    for i in range(5):
        tweets.append(twit_json_body["statuses"][twit_random+i]['id'])

    return flask.render_template(
        "sabich.html",
        title = spoonacular_json_body[random_recipie]["title"],
        image = spoonacular_json_body[random_recipie]["image"],
        ingredients_list = spoonacular_json_body[random_recipie]["extendedIngredients"],
        steps_list = spoonacular_json_body[random_recipie]["analyzedInstructions"][0]["steps"],
        tweet_ids = tweets,
        )

app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0'),
    debug = True
    )