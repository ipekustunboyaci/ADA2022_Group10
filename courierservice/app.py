from flask import Flask, request

from db import Base, engine
from resources.courier import Courier

app = Flask(__name__)
app.config["DEBUG"] = True
Base.metadata.create_all(engine)


@app.route('/couriers', methods=['POST'])
def create_courier():
    req_data = request.get_json()
    return Courier.create_courier(req_data)


@app.route('/couriers/<c_id>', methods=['GET'])
def get_delivery(c_id):
    return Courier.get_courier(c_id)


@app.route('/couriers/<c_id>/status', methods=['PUT'])
def update_courier_status(c_id):
    status = request.args.get('status')
    return Courier.update_courier_status(c_id, status)

@app.route('/couriers/<c_id>', methods=['DELETE'])
def delete_courier(c_id):
    return Courier.delete_courier(c_id)


app.run(host='0.0.0.0', port=5000)