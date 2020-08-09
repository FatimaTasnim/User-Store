from .db import db
import uuid


def generate_uuid():
    return (uuid.uuid4().hex)
class User(db.Document):
    user_id = db.StringField(unique=True, default=generate_uuid, immutable=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    role = db.ListField(db.StringField(), required=True)
    parent = db.StringField(required=False) 
    state = db.StringField(required=False)
    street = db.StringField(required=False)
    city = db.StringField(required=False)
    zip = db.StringField(required=False)