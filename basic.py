from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
        {
            'name': 'My Wonderful Store',
            'items': [
                {
                    'name': 'something',
                    'price': 750000
                }
            ]
        }
    ]

@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)

    return jsonify(new_store)


@app.route('/store/<string:name>')
def get_store(name):
    for item in stores:
        if item['name'] == name:
            return jsonify(item)
    return jsonify({'msg': 'There was an error...'})

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for item in stores:
        if item['name'] == name:
            item['items'].append({'name': request_data['name'], 'price': request_data['price']})
            return jsonify(item)
    return jsonify({'msg': 'There was an error...'})

@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for item in stores:
        if item['name'] == name:
            return jsonify({'items': item['items']})
    return jsonify({'msg': 'There was an error...'})

if __name__ == '__main__':
    app.run(port=5000)