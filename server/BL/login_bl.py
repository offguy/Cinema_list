from flask import jsonify
from DAL.persons_dal import PersonsDAL

class LoginBL():
    def __init__(self):
        self.persons_dal = PersonsDAL()

    def login(self, per):
        persons = self.persons_dal.get_all_persons()
        filtered_person = [p for p in persons if p["name"] == per["name"] and p["password"] == per["password"]]
        if filtered_person:
            return jsonify({"message": "Logged in!", "status": "success", "id" : filtered_person[0]["id"]})
        else:
            return jsonify({"message": "Denied", "status": "failure", "id": None})
