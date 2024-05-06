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
        persons.append(obj)
        self.persons_dal.save_persons(persons)
        return jsonify(f"person {obj['name']} created")


    def update_person(self, id, obj):
        persons = self.persons_dal.get_all_persons()
        for p in persons:
            if p["id"] == int(id):
                p["name"] = obj["name"]
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
                    if len(exist) == 0:
                        p["movie_list"].append(obj["title"])
                        break
                    return jsonify(f"movie already in {p["name"]}'s list")
            self.persons_dal.save_persons(persons)
            return jsonify(f"movie {obj["title"]} added to {p["name"]}'s movies list")       
