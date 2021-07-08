import json
from urllib.request import urlopen
from urllib.request import Request, urlopen 

class Post():
    """
    A simple ViewSet for listing or retrieving post.
    """
    def list_objects(self):
        data = json.load(urlopen('https://jsonplaceholder.typicode.com/posts'))
        return data 
    
    def retrieve(self, id=None):
        data = json.load(urlopen('https://jsonplaceholder.typicode.com/posts/' + str(id)))
        return data