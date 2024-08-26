from DAL.persons_dal import PersonsDAL
from flask import jsonify

class PersonsBL():
    def __init__(self) -> None:
        self.persons_dal = PersonsDAL()

    def get_all_persons(self):
        return jsonify(self.persons_dal.get_all_persons())
    
    def get_person_by_id(self, id):
        persons = self.persons_dal.get_all_persons()
        person = list(filter(lambda x: x["id"] == int(id), persons))[0]
        return jsonify(person)
    
    def add_new_person(self, obj):
        persons = self.persons_dal.get_all_persons()
        if list(filter(lambda x: x["id"] == int(obj["id"]), persons)):
            return jsonify({"error": f"id {obj['id']} already exists"}), 400
        elif list(filter(lambda x: x["name"] == obj["name"], persons)):
            return jsonify({"error": f"name {obj['name']} already exists"}), 400
        else:
            obj["movie_list"] = []
            persons.append(obj)
            self.persons_dal.save_persons(persons)
            return jsonify({"message": f"person {obj['name']} created"}), 201
    
    def update_person(self, id, obj):
        persons = self.persons_dal.get_all_persons()
        for p in persons:
            if p["id"] == int(id):
                p["name"] = obj["name"]
                p["password"] = obj["password"]
                p["movie_list"] = obj["movie_list"]
                break
        self.persons_dal.save_persons(persons)        
        return jsonify("person updated")
    
    def delete_persons(self, id):
        persons = self.persons_dal.get_all_persons()
        new_persons = list(filter(lambda x: x["id"] != int(id), persons))
        self.persons_dal.save_persons(new_persons)
        return jsonify(f"person {id} deleted")
    
    def add_movie_to_person_list(self, id, obj):
        persons = self.persons_dal.get_all_persons()
        for p in persons:
            if p["id"] == int(id):
                exist = list(filter(lambda x: x == obj["title"], p["movie_list"]))
                if len(exist) != 0:
                    return jsonify(f"Movie already in {p['name']}'s list")
                p["movie_list"].append(obj["title"])
                self.persons_dal.save_persons(persons)
                return jsonify(f"Movie {obj['title']} added to {p['name']}'s movies list")
        
        return jsonify(f"Person with ID {id} not found")
