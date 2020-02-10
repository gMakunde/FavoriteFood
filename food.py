import flask
import twitter_data, recipie_data
import os
import random

app = flask.Flask(__name__)


@app.route('/')
def index():
    """
    A function that renders an HTML template that displays recipe information 
    and quotes.
    
    This function dynamicly fetches quotes about israeli food using the twitter 
    api and dynamicly fetches recipie directions and ingredients using the 
    spoonacular api.
    
    Returns:
        str: Result of evaluating israeli_food.html file.
    """
    
    twit = twitter_data.TwitterData()
    twit_json_body = twit.get_json()
    tweets = twit.get_random_tweets(twit_json_body)
    
    spoon = recipie_data.RecipieData()
    sabich_query = "https://api.spoonacular.com/recipes/search?query=sabich"
    falafel_query = "https://api.spoonacular.com/recipes/search?query=falafel"
    hummus_query = "https://api.spoonacular.com/recipes/search?query=hummus"
    queries = [sabich_query, falafel_query, hummus_query]
    spoon.group_queries(queries)
    spoonacular_json_body = spoon.get_json()
    random_recipie = random.randint(0, len(spoonacular_json_body)-1)


    return flask.render_template(
        "israeli_food.html",
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