from DAL.movies_dal import MoviesDAL
from flask import jsonify

class MoviesBL():
    def __init__(self):
        self.movies_dal = MoviesDAL()

    def get_all_movies(self):
        data = self.movies_dal.get_all_movies_data()
        movies = list(map(lambda x: {
            "title": x["name"],
            "rating": x["rating"]["average"],
            "image": x["image"]["medium"],
        }, data))
        return jsonify(movies)