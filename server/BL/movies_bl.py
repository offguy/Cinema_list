from REPO.movies_rep import MoviesREP
from flask import jsonify

class MoviesBL():
    def __init__(self):
        self.movies_rep = MoviesREP()

    def get_all_movies(self):
        data = self.movies_rep.get_all_movies_data()
        movies = list(map(lambda x: {
            "title": x["name"],
            "rating": x["rating"]["average"],
            "image": x["image"]["medium"],
        }, data))
        return jsonify(movies)