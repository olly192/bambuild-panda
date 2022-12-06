import json

from flask import Blueprint, request
from flask_cors import cross_origin

from server.app import db
from server.helper import generate_order_identifer
from server.models import Order

api = Blueprint('api', __name__)


# Order API
@api.route('/create-order/<product_identifier>', methods=['POST'])
@cross_origin()
def create_order(product_identifier):
    data = request.json
    details = {
        'engravings': data['engravings'],
        'insert': data['insertCode'],
    }
    try:
        order = Order(
            identifier=generate_order_identifer(),
            product_identifier=product_identifier,
            details=details,
            email=data['email'],
            firstname=data['firstName'],
            lastname=data['lastName'],
            status=0,
            shipping_method=int(data['shippingMethod']),
            shipping_details=data['shippingDetails']
        )
    except KeyError:
        return {'error': 'Invalid options.'}, 400
    db.session.add(order)
    db.session.commit()
    return json.dumps({'identifier': order.identifier}), 200, {'ContentType': 'application/json'}


@api.route('/link-order', methods=['POST'])
@cross_origin()
def link_order():
    order = Order.query.filter_by(identifier=request.json['identifier']).first()
    if order.ye_order_number:
        return json.dumps({'error': 'Order already linked'}), 400, {'ContentType': 'application/json'}
    order.ye_order_number = request.json['orderNumber']
    db.session.commit()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
