import requests
import os

class RecipieData:
    """
A class used to return recipie json from multiple queries

...

Attributes
----------
url: str
a string containing spoonacular Get Recipe Information Bulk api endpoint. 
the default endpoint has no ids.
key: str
spoonacular api key

Methods
--------
group_queries()
appends every result's id to the url
get_json()
returns json body of the endpoint
"""
    def __init__(self, key):
        """
Parameters
----------
url: str
a string containing spoonacular Get Recipe Information Bulk api endpoint. 
the default endpoint has no ids.
key: str
spoonacular api key
"""
        self.url = "https://api.spoonacular.com/recipes/informationBulk?ids="
        self.key = key
    
    def group_queries(self, url_list):
        """appends every result's id to the url.

Parameters
-----------
url_list: list
list of strings that contain Search Recipes endpoints from spoonacular api
"""
        responses = []
        for urls in url_list:
            responses.append(requests.get(urls + self.key).json())
            
        for response in responses:
            for i in range(len(response['results'])-1):
                self.url += str(response["results"][i]["id"]) + ","

    def get_json(self):
        """returns json body of the endpoint

Returns
--------
json
json body that contains recipie information from one or more queries
"""
        return requests.get(self.url + self.key).json() 


