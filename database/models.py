from .db import db


class User(db.Document):
    id = db.StringField(required = True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    role = db.ListField(db.StringField(), required=True)
    parent = db.StringField(required=False) 
    state = db.StringField(required=False)
    street = db.StringField(required=False)
    city = db.StringField(required=False)
    zip = db.StringField(required=False)