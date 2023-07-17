from marshmallow import Schema, fields

#Schema is used to validate incoming data

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)