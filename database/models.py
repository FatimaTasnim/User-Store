import uuid

from .db import db


def generate_uuid():
    return uuid.uuid4().hex


USER_ROLE = ("PARENT", "CHILD")


class User(db.Document):
    user_id = db.StringField(unique=True, default=generate_uuid, immutable=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    role = db.StringField(choices=USER_ROLE, required=True, immutable=True)
    parent = db.StringField(required=False, immutable=True)
    state = db.StringField(required=False)
    street = db.StringField(required=False)
    city = db.StringField(required=False)
    zip = db.StringField(required=False)
