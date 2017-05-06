import hug
import json

from datetime import datetime
from dateutil import relativedelta as rdelta
from database import User, MainDatabase

@hug.post('/user/signup')
def user_signup(body, charset='utf-8'):

    user = User(**body)
    user.save()

    return json.loads(user.to_json())


@hug.get('/user/age')
def user_age(id, charset='utf-8'):

    query = User.objects(id=id)

    if len(query) > 0:

        user = query.get(0)
        rd = rdelta.relativedelta(datetime.now(), user.birthday)

        return {
            'age': "{0.years} years, {0.months} months, {0.days} days".format(rd),
            'user': json.loads(user.to_json())
        }



@hug.get('/user/find')
def user_age(id, charset='utf-8'):
    return json.loads(User.objects(id=id).to_json())


@hug.startup()
def start(api):
    db = MainDatabase({})
    db.connect()
