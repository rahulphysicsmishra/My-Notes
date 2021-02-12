import json

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not json serializable ')
userJSON = json.dumps(user, default=encode_user)  # this will give error if we dont define encode func ...
print(userJSON)

#another way of encoding userJSON
from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON2 = UserEncoder().encode(user)
print(userJSON2)

user = json.loads(userJSON)
print(user, type(user))  # we cannot call name by object method (user.name) bcos it is of type dict,  so we will have to define custom decoding method

# Now we will define def decode func
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
print(user.name)