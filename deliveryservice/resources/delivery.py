from datetime import datetime

from flask import jsonify


from daos.delivery_dao import DeliveryDAO

from db import Session


class Delivery:
    @staticmethod
    def create(body):
        session = Session()
        delivery = DeliveryDAO(body['order_id'], datetime.strptime(body['delivery_time'], '%Y-%m-%d %H:%M:%S.%f'),
                               body['delivery_address'], body['status'], datetime.now())
        session.add(delivery)
        session.commit()
        session.refresh(delivery)
        session.close()
        return jsonify({'Delivery created with id:': delivery.id}), 200

    @staticmethod
    def get(d_id):
        session = Session()
        delivery = session.query(DeliveryDAO).filter(DeliveryDAO.id == d_id).first()

        if delivery:
            status_obj = delivery.status
            text_out = {
                "order_id": delivery.order_id,
                "delivery_time": delivery.delivery_time.isoformat(),
                "delivery_address": delivery.delivery_address,
                "status": delivery.status,
                "status_last_update": delivery.status_last_update.isoformat()
            }
            session.close()
            return jsonify(text_out), 200
        else:
            session.close()
            return jsonify({'message': f'There is no delivery with id {d_id}'}), 404

    @staticmethod
    def delete(d_id):
        session = Session()
        effected_rows = session.query(DeliveryDAO).filter(DeliveryDAO.id == d_id).delete()
        session.commit()
        session.close()
        if effected_rows == 0:
            return jsonify({'message': f'There is no delivery with id {d_id}'}), 404
        else:
            return jsonify({'message': 'The delivery was removed'}), 200

    def update_delivery_time(d_id, new_delivery_time):
        session = Session()
        delivery = session.query(DeliveryDAO).filter(DeliveryDAO.id == d_id)[0]
        delivery.delivery_time = new_delivery_time
        session.commit()
        return jsonify({'message': 'The delivery time was updated'}), 200

    def update_delivery_status(d_id, status):
        session = Session()
        delivery = session.query(DeliveryDAO).filter(DeliveryDAO.id == d_id)[0]
        delivery.status = status
        delivery.status_last_update = datetime.now()
        session.commit()
        return jsonify({'message': 'The delivery status was updated'}), 200