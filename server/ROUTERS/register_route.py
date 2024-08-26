from flask import Blueprint, request
from BL.pesrons_bl import PersonsBL

register_route = Blueprint("register_route", __name__)
PersonsBL = PersonsBL()

@register_route.route("/register", methods=["POST"])
def register():
    per = request.json
    response = PersonsBL.add_new_person(per)
    return response
