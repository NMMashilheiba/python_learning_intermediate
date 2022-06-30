import json

person = {"name": "John", "age": 30, "city": "New York",
        "has children": False, "titles": ["Engineer", "Programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)
print(personJSON)

#with open('persona.json', 'w') as file:
#    json.dump(person, file)

person = json.loads(personJSON)
print(person)