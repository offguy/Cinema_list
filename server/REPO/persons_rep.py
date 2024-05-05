import json, os, sys


class PersonsREP():
    def __init__(self) -> None:
        self.__path = os.path.join(sys.path[0], "DATA\\persons.json")

    def get_all_persons(self):
        with open(self.__path) as f:
            data = json.load(f)
            persons = data["persons"]
            return persons
        
    def save_persons(self, obj):
        with open(self.__path, "w") as f:
            json.dump({"persons": obj}, f, indent=0)
            return "saved to file"