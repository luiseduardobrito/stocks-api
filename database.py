from mongoengine import connect, Document, StringField


class MainDatabase:
    def __init__(self, options):
        self.options = options

    def connect(self):
        connect('stocks-api', host='mongodb://localhost/stocks-api')


class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=32, required=True)
    password = StringField(max_length=16, required=True)
