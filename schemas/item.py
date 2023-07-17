from marshmallow import Schema, fields

#Schema is used to validate incoming data

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.String(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
