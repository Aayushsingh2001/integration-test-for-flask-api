from flask import Flask, request, jsonify
from db import init_db, get_items, add_item

app = Flask(__name__)
init_db()

@app.route('/items', methods=['GET'])
def get():
    return jsonify(get_items())

@app.route('/items', methods=['POST'])
def post():
    data = request.get_json()
    add_item(data['name'])
    return jsonify({'message': 'Item added'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0')
