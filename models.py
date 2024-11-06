import datetime
from app import db

class Order(db.Model):
    tablename = ['Suggestions']
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    order = db.Column(db.String())
    notes = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_confirmed = db.Column(db.DateTime, default=datetime.now())
    date_delivered = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String())
    paid = db.Column(db.Boolean())




