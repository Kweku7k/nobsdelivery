from datetime import datetime
from extensions import db

class Order(db.Model):
    tablename = ['Suggestions']
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    phone = db.Column(db.String())
    location = db.Column(db.String())
    order = db.Column(db.String())
    notes = db.Column(db.String())
    date_created = db.Column(db.DateTime, default=datetime.now())
    date_confirmed = db.Column(db.DateTime, default=datetime.now())
    date_delivered = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.String())
    paid = db.Column(db.Boolean())

    def __repr__(self):
        return '<Order %r>' % self.id
    
    def new_order():   
        try:
            order = Order(user="XXXX", order="test", notes="test", status="test", paid=False)
            db.session.add(order)
            db.session.commit()
        except Exception as e:
            print(e)
            
        return order

class DeliveryRider(db.Model):
    __tablename__ = 'delivery_riders'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    telegram_token = db.Column(db.String(100))
    phone_number = db.Column(db.String(15), unique=True)
    active = db.Column(db.Boolean, default=True)
    successful_deliveries = db.Column(db.Integer, default=0)
    last_seen = db.Column(db.DateTime, default=datetime.now())
    
    def __repr__(self):
        return f"<DeliveryRider {self.name}>"
    

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'telegram_token': self.telegram_token,
            'phone_number': self.phone_number,
            'active': self.active,
            'successful_deliveries': self.successful_deliveries,
            'last_seen': self.last_seen
        }
    
    @classmethod
    def get_available_riders(cls):
        return cls.query.filter_by(active=True).all()
    
    
    


