import hug
import json

from database import User, MainDatabase

@hug.post('/signup', output=hug.output_format.json)
def user_signup(body, charset='utf-8'):

    user = User(email=body['email'], name=body['name'], password=body['password'])
    user.save()

    return json.loads(user.to_json())


@hug.get('/user/age', output=hug.output_format.json)
def user_age(body, charset='utf-8'):





db = MainDatabase({})
db.connect()
