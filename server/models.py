from server.app import db
from flask_login import UserMixin


# User database model
class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256), unique=True)
    profile = db.Column(db.LargeBinary)
    hashed_password = db.Column(db.String(256))
    active = db.Column(db.Boolean, default=True)
    read_only = db.Column(db.Boolean, default=True)
    admin = db.Column(db.Boolean, default=False)


# Order database model
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(256), unique=True, nullable=False)
    product_identifier = db.Column(db.String)
    details = db.Column(db.JSON)
    email = db.Column(db.String)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    ye_order_number = db.Column(db.Integer)
    status = db.Column(db.Integer)
    # Status codes:
    # 0: Order submitted
    # 1: Order linked and awiaitng payment
    # 2: Order paid for
    # 3: Order processing (being built)
    # 4: Order shipped
    # 5: Order delivered
    # 6: Order cancelled - see details
    # 7: Order refunded - see details
    # 8: Order returned - see details
    # 9: Other - see details
    status_details = db.Column(db.UnicodeText)
    shipping_method = db.Column(db.Integer)
    # Shipping method codes:
    # 0: In-person delivery
    # 1: Mail delivery
    shipping_details = db.Column(db.JSON)
    submitted = db.Column(db.DateTime, default=db.func.now())
    users = db.Column(db.ARRAY(db.Integer))


class Image(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(256), unique=True, nullable=False)
    image = db.Column(db.LargeBinary)
    mimetype = db.Column(db.String(256))


class MarketOrder(db.Model):
    __tablename__ = 'market_order'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    payment_method = db.Column(db.String(256), nullable=False)
    order_items = db.Column(db.JSON, nullable=False)
    total = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(256), nullable=True)



