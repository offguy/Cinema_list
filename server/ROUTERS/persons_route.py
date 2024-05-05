from flask import Blueprint, request
from BL.pesrons_bl import PersonsBL

persons_route = Blueprint("persons_route", __name__)
persons_bl = PersonsBL()

@persons_route.route("/persons", methods=["GET"])
def get_all_movies():
    return persons_bl.get_all_persons()

@persons_route.route("/persons/<string:id>", methods=["GET"])
def get_person_by_id(id):
    return persons_bl.get_person_by_id(id)

@persons_route.route("/persons", methods=["POST"])
def add_new_person():
    obj = request.json
    return persons_bl.add_new_person(obj)

@persons_route.route("/persons/<string:id>", methods=["DELETE"])
def delete_person(id):
    return persons_bl.delete_persons(id)

@persons_route.route("/persons/<string:id>", methods=["PUT"])
def update_person(id):
    obj = request.json
    return persons_bl.update_person(id, obj)

@persons_route.route("/persons/<string:id>", methods=["POST"])
def add_movie_to_person_list(id):
        obj = request.json
        return persons_bl.add_movie_to_person_list(id, obj)

