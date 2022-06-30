import json

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 26)
#custom encoder func()

def encoder_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

from json import JSONEncoder

class UserEncoder(JSONEncoder):    
    def default(self, obj):
        if isinstance(obj, User):
            return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


#userJSON = json.dumps(user, default= encoder_user)     
userJSON = json.dumps(user, cls=UserEncoder)  
#or use UserEncoder() directly
userJSON_1 = UserEncoder().encode(user)
print(userJSON)   
#print(userJSON_1)

def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook= decode_user)
#print(type(user))
print(user.name, user.age)