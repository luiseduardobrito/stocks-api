import hug
import json

from database import User, MainDatabase

@hug.get('/happy_birthday', output=hug.output_format.json)
def happy_birthday(name, age: hug.types.number = 1):
    return {
        'name': name,
        'age': age
    }


@hug.post('/signup', output=hug.output_format.json)
def signup(body, charset='utf-8'):

    user = User(email=body['email'], name=body['name'], password=body['password'])
    user.save()

    return json.loads(user.to_json())


db = MainDatabase({})
db.connect()
