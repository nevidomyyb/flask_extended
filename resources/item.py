from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask import request
from schemas import ItemSchema, ItemUpdateSchema
import uuid

blp = Blueprint("items", __name__, description="Items operations")

@blp.route('/item/<item_id>/')
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id], 200
        except KeyError:
            abort(404,message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404,message="Item not found")

    @blp.arguments(ItemUpdateSchema)    
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(400, message="Item not found.")

@blp.route('/item/')
class ItemList(MethodView):

    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()
    
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        for item in items.values():
            if (item_data["name"] == item["name"] 
            and item_data["store_id"] == item["store_id"]):
                abort(400, message="Item already exist")
        
        if item_data["store_id"] not in stores:
            abort(404,message="Store not found")
        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item