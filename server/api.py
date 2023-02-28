import json

from flask import Blueprint, request, render_template
from flask_cors import cross_origin

from server.app import db
from server.helper import generate_identifer
from server.models import Order, Image, MarketOrder

api = Blueprint('api', __name__)


# Order API
@api.route('/order-lightbox/<product_identifier>', methods=['POST'])
@cross_origin()
def create_order(product_identifier):
    data = request.json
    try:
        order = Order(
            identifier=generate_identifer(),
            product_identifier="lightbox-" + product_identifier,
            details={
                'engravings': data['engravings'],
                'insert': data['insertCode'],
                'payment_method': int(data["paymentMethod"]),
            },
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


@api.route('/order-image/<product_identifier>', methods=['POST'])
@cross_origin()
def order_keyring(product_identifier):
    import base64
    try:
        image = Image(
            identifier=generate_identifer(),
            image=base64.b64encode(request.files['image'].read()),
            mimetype=request.files['image'].mimetype
        )
        order = Order(
            identifier=generate_identifer(),
            product_identifier=product_identifier,
            details={
                'image': image.identifier,
                'instructions': request.form.get("instructions"),
                'payment_method': int(request.form.get("paymentMethod"))
            },
            email=request.form.get("email"),
            firstname=request.form.get("firstName"),
            lastname=request.form.get("lastName"),
            status=0,
            shipping_method=int(request.form.get("shippingMethod")),
            shipping_details=request.form.get("shippingDetails")
        )
    except KeyError:
        return {'error': 'Invalid options.'}, 400
    db.session.add(image)
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


@api.route('/get-order-details/<identifier>')
@cross_origin()
def get_order_details(identifier):
    order = Order.query.filter_by(identifier=identifier).first()
    if order:
        if 'image' in order.details.keys() and order.details['image']:
            image = Image.query.filter_by(identifier=order.details['image']).first()
        else:
            image = None
        return render_template("order_details.html", page="order-details", order=order, image=image)
    return {'error': 'Invalid identifier.'}, 400


@api.route('/submit-market-order', methods=['POST'])
@cross_origin()
def submit_market_order():
    data = request.form
    market_order = MarketOrder(
        payment_method=request.form.get("payment_method"),
        order_items=json.loads(request.form.get("order_items")),
        total=request.form.get("total"),
        email=request.form.get("email") or None,
    )
    db.session.add(market_order)
    db.session.commit()
    print(data)
    return "True", 200
