import json

from flask import Blueprint, request
from flask_cors import cross_origin

from server.app import db
from server.models import Order

api = Blueprint('api', __name__)


# Order API
@api.route('/submit-order/<product_identifier>', methods=['POST'])
@cross_origin()
def submit_order(product_identifier):
    data = request.json
    details = {
        'engravings': data['engravings'],
        'insert': data['insertCode'],
    }
    order = Order(
        product_identifier=product_identifier,
        details=details,
        email=data['email'],
        firstname=data['firstName'],
        lastname=data['lastName'],
        ye_order_number=data['orderNumber'],
        status=0,
        shipping_method=int(data['shippingMethod']),
        shipping_details=data['shippingDetails']
    )
    db.session.add(order)
    db.session.commit()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
