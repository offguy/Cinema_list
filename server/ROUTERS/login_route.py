from flask import Blueprint, request
from BL.login_bl import LoginBL

login_route = Blueprint("login_route", __name__)
login_bl = LoginBL()

@login_route.route("/login", methods=["POST"])
def login():
    per = request.json
    return login_bl.login(per)

