import datetime
from flask import jsonify

from daos.courier_dao import CourierDAO
from db import Session

# Courier crud actions in database
class Courier:

    @staticmethod
    def create_courier(body):
        session = Session()
        courier = CourierDAO(body['name'], body['store_id'], body['status'])
        session.add(courier)
        session.commit()
        session.refresh(courier)
        session.close()
        return jsonify({'courier_id': courier.id}), 200

    def get_courier(c_id):
        session = Session()
        courier = session.query(CourierDAO).filter(CourierDAO.id == c_id).first()

        if courier:
            status_obj = courier.status
            text_out = {
                "courier_id:": courier.id,
                "courier_name": courier.name,
                "store_id": courier.store_id,
                "status": courier.status
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no courier with id {c_id}'}), 404

    def update_courier_status(c_id, status):
        session = Session()
        courier = session.query(CourierDAO).filter(CourierDAO.id == c_id).first()
        courier.status = status
        #courier.status.last_update = datetime.datetime.now()
        session.commit()
        return jsonify({'message': 'The courier status was updated'}), 200

    def delete_courier(c_id):
        session = Session()
        effected_rows = session.query(CourierDAO).filter(CourierDAO.id == c_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no courier with id {c_id}'}), 404
        else:
            return jsonify({'message': 'The courier was removed'}), 200