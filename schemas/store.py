from marshmallow import Schema, fields
from schemas.item import PlainItemSchema

#Schema is used to validate incoming data

class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)