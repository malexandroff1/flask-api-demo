from marshmallow import Schema
from marshmallow import fields

class UserSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    birthdate = fields.Date(required=True)
