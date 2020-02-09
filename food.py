import flask
import twitter_data, recipie_data
import os
import random

app = flask.Flask(__name__)


@app.route('/')
def index():
    
    twit_url = "https://api.twitter.com/1.1/search/tweets.json?q=falafel%20hummus&result_type=mixed"
    twit = twitter_data.TwitterData(twit_url, "KJFYSqLhZ8rwQiXJsvkjN9GzF", "J7G5iZndpRmiH5tzihuJxHQe0nDYpxvVhQ1W4v9OOpQrujurXn", "519031926-OmiqDkHu7pIaLSZqRknbD5fp9uwFF9m4ah2ZPypC", "HOcM2UpzwoVVlxTmD1tihORc9hWGcJatOW1cK1Z6GaVMv")
    # twit = twitter_api.TwitterData(twit_url, os.getenv('twit_key'), os.getenv('twit_secret'), os.getenv('twit_token')), os.getenv('twit_token_secret')
    twit_json_body = twit.get_json()
    tweets = twit.get_random_tweets(twit_json_body)
    
    spoonacular_url = "https://api.spoonacular.com/recipes/informationBulk?ids="
    spoon = recipie_data.RecipieData(spoonacular_url, "&apiKey=0df474a2434e4aefacf96e34ba4a7761")
    # spoon = spoonacular_api.RecipieData(spoonacular_url, os.getenv('spoonKey'))
    sabich_query = "https://api.spoonacular.com/recipes/search?query=sabich"
    falafel_query = "https://api.spoonacular.com/recipes/search?query=falafel"
    hummus_query = "https://api.spoonacular.com/recipes/search?query=hummus"
    queries = [sabich_query, falafel_query, hummus_query]
    spoon.group_queries(queries)
    spoonacular_json_body = spoon.get_json()
    
    
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