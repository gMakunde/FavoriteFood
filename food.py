import flask
import os
import random
import requests, requests_oauthlib
import os
import random

app = flask.Flask(__name__)


@app.route('/')
def index():
    twit_url = "https://api.twitter.com/1.1/search/tweets.json?q=falafel%20hummus&result_type=mixed"
    twit_key = os.getenv('twit_key')
    twit_secret = os.getenv('twit_secret')
    twit_token = os.getenv('twit_token')
    twit_token_secret = os.getenv('twit_token_secret')
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
    twit_json_body = requests.get(twit_url, auth=twit_oauth).json()
    twit_random = random.randint(0, len(twit_json_body["statuses"])-5)
    tweets = []
    for i in range(5):
        tweets.append(twit_json_body["statuses"][twit_random+i]['id'])
    
    sabich_query = "https://api.spoonacular.com/recipes/search?query=sabich"
    falafel_query = "https://api.spoonacular.com/recipes/search?query=falafel"
    hummus_query = "https://api.spoonacular.com/recipes/search?query=hummus"
    spoonacular_url = "https://api.spoonacular.com/recipes/informationBulk?ids="
    #spoonacular_key = os.getenv('spoonKey')
    spoonacular_key = "&apiKey=0df474a2434e4aefacf96e34ba4a7761"
    sabich_json = requests.get(sabich_query + spoonacular_key).json()
    falafel_json = requests.get(falafel_query + spoonacular_key).json()
    hummus_json = requests.get(hummus_query + spoonacular_key).json()
    
    for i in range(len(sabich_json["results"])-1):
        spoonacular_url += str(sabich_json["results"][i]["id"]) + ","
    for i in range(len(falafel_json["results"])-1):
        spoonacular_url += str(falafel_json["results"][i]["id"]) + ","
    for i in range(len(hummus_json["results"])-1):
        spoonacular_url += str(hummus_json["results"][i]["id"]) + ","
    
    spoonacular_json_body = requests.get(spoonacular_url + spoonacular_key).json()    
    random_recipie = random.randint(0, len(spoonacular_json_body)-1)
    
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