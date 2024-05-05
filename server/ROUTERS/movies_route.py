from flask import Blueprint
from BL.movies_bl import MoviesBL

movies_route = Blueprint("movies_route", __name__)
movies_bl = MoviesBL()

@movies_route.route("/movies", methods=["GET"])
def get_all_movies():
    return movies_bl.get_all_movies()