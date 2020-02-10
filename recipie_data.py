import requests
import os

class RecipieData:
    """
    A class used to return a single json body from multiple recipe queries.
    
    Attributes:
        url (str): A string containing the spoonacular "Get Recipe Information Bulk" api endpoint. The default endpoint has no ids.
        key (str): A spoonacular api key.
    """
    def __init__(self):
        """
        The constructor for the RecipieData class.
        """
        self.url = "https://api.spoonacular.com/recipes/informationBulk?ids="
        self.key = os.getenv('spoonKey')
    
    def group_queries(self, url_list):
        """
        A method that appends every result's id to self.url.

        Parameters:
            url_list (list): A list of strings that contain "Search Recipes" endpoints from the spoonacular api.
        """
        responses = []
        for urls in url_list:
            responses.append(requests.get(urls + self.key).json())
            
        for response in responses:
            for i in range(len(response['results'])-1):
                self.url += str(response["results"][i]["id"]) + ","

    def get_json(self):
        """
        A method that returns the json body of the grouped recipie queries.

        Returns:
            dict: json body that contains recipie information from one or more queries
        """
        return requests.get(self.url + self.key).json() 


