import requests

class MoviesDAL():
    def __init__(self):
        self.__url = "https://api.tvmaze.com/shows"

        
    def get_all_movies_data(self):
        resp = requests.get(self.__url)
        return resp.json()