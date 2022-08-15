from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "Nisanth77131477!"
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        
        return item, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is None:
            parser = reqparse.RequestParser()
            parser.add_argument('price', type=float, required=True)
            data = parser.parse_args()
            item = {'name': name, 'price': data['price']}
            items.append(item)
            return item, 201
        else:
            return None, 400

    def delete(self, name):
        global items

        items2 = []

        for x in items:
            if x['name'] != name:
                items2.append(x)

        items = items2

    def put(self, name):
        global items
        parser = reqparse.RequestParser()
        parser.add_argument('price', type=float, required=True)
        data = parser.parse_args()
        item = {'name': name, 'price': data['price']}

        matching_item = next(filter(lambda x: x['name'] == name, items), None)

        if matching_item is None:
            items.append(item)
        else:
            matching_item.update(item)

        return item, 201

class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, "/items")

app.run(debug=True)