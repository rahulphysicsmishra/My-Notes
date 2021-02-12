import json

person = {"name": "John", "age": 38, "city": "New York", "haschildren": False, "titles": ["engineer", "programmer"]}

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)