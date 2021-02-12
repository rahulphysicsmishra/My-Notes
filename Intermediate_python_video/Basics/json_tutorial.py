import json

person = {"name": "John", "age": 38, "city": "New York", "haschildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, sort_keys=True)  # converting dict to json
print(personJSON)

person = json.loads(personJSON)  # converting json back to dict
print(person)