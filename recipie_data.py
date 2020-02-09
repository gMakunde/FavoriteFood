import requests


class RecipieData:
    def __init__(self, url, key):
        self.url = url
        self.key = key
    
    def group_queries(self, url_list):
        responses = []
        for urls in url_list:
            responses.append(requests.get(urls + self.key).json())
            
        for response in responses:
            for i in range(len(response['results'])-1):
                self.url += str(response["results"][i]["id"]) + ","

    def get_json(self):
        return requests.get(self.url + self.key).json() 


