import json
import os
import pprint
from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
from apiresponse import ApiResponse
from forms import Delivery
# from services import createOrder
from extensions import db  # Import from extensions instead of app
from utils import send_message
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SECRET_KEY'] = 'c2ba24216b13s5e0c676d8b8021579fde'
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DELIVERY_DB_URL')

db.init_app(app)
migrate = Migrate(app, db)

print(app.config['SQLALCHEMY_DATABASE_URI'])

from models import *


@app.route('/',methods=['GET','POST'])
async def details(): 
    form = Delivery()
    if request.method == 'POST':
        # create an order and send broadcast
        if form.validate_on_submit():
            print(form.data)
            data = form.data

            print(type(data))

            order = Order(
                user = data.get('name'),
                phone = data.get('phone'),
                location = data.get('location'),
                order = data.get('description'),
                notes = data.get('notes'),
                status = "pending",
                paid = False
            )
            
            await send_message(text=form.data)
            
            try:
                db.session.add(order)
                db.session.commit()

                # send the order to the rider   
                await send_message(chat_id="2082809928",text=f"New Order: {order.user} - {order.phone} - {order.location} - {order.order} - {order.notes}")

                return redirect(url_for('order_details', id=order.id))
            except Exception as e:
                print(e)
            
        else:
            print(form.errors)
    return render_template('index.html', form=form)

# 
@app.route('/order_details/<int:id>', methods=['GET', 'POST'])
def order_details(id):
    order = Order.query.get_or_404(id)
    return render_template('order_details.html', order = order)

# prompt: write an api that takes a rider token and a rider active status ie True or False
@app.route('/rider/<string:token>/<int:active>', methods=['GET', 'POST'])
async def rider_status(token, active):
    request_body = request.json
    print("-----")

    pprint.pprint(request_body)
    print(type(request_body))

    if request_body:
        body = json.loads(request_body)
    else:
        body = None

    pprint.pprint(body)
    print(type(body))
    

    print(f"Attempting to find Rider: {token}")
    rider = DeliveryRider.query.filter_by(telegram_token=token).first()
    if rider:
        print("Rider Found: ",rider.to_dict())
        try:
            rider.active = active
            db.session.commit()
            response = ApiResponse(data = rider.to_dict(), message="Rider created", code=200, status="Successfi;").to_dict()
            print(response)
            await send_message(text=f"Rider: {rider.name} Status has been set to active")
            return response
        except Exception as e:
            print(e)
            response = ApiResponse(data = rider.to_dict(), message="Rider created", code=400, status="Failed;").to_dict()

    else:

        try:
            rider = DeliveryRider(telegram_token=token, active=active, name=body.get('username'))
            db.session.add(rider)
            db.session.commit()

            message = f"Registered User: {rider.name} Status has been set to active"

            await send_message(text=message)
            
            response = ApiResponse(data = rider.to_dict(), message="Rider created", status=200).to_dict()
            return response

        except Exception as e:
            print(e)

        return "Rider created"
    

    



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, host='0.0.0.0', debug=True)