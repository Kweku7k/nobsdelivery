import json
import os
import pprint
from flask import Flask, flash,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
import urllib
from apiresponse import ApiResponse
from forms import Delivery
# from services import createOrder
from extensions import db  # Import from extensions instead of app
from utils import send_message
from flask_migrate import Migrate



app=Flask(__name__)
app.config['SECRET_KEY'] = 'c2ba24216b13s5e0c676d8b8021579fde'
# app.config['SQLALCHEMY_DATABASE_URI']= "postgresql://ohene:ohene_db_2024$$$@localhost:5432 /delivery"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


db.init_app(app)
migrate = Migrate(app, db)

print(app.config['SQLALCHEMY_DATABASE_URI'])
from models import *


def votingAlert(params):
    try:
        url = "https://api.telegram.org/bot5885119922:AAEN5JGeqkIza_kgc3eObzJuCdV3FK_9BsE/sendMessage?chat_id=-903004895&text=" + urllib.parse.quote(params)
        content = urllib.request.urlopen(url).read()
        app.logger.info(content)
        return content
    except Exception as e:
        app.logger.info(e)
        return e

@app.errorhandler(500)
def internal_server_error(error):
    votingAlert(str(error) + "\n" + str(request.url) + "\n" )
    return render_template('500.html'), 500






@app.route('/cu15',methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
async def details(): 
    form = Delivery()
    if request.method == 'POST':
        # create an order and send broadcast
        if form.validate_on_submit():
            
            current_date = datetime.now()
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
                date_created = current_date,
                paid = False
            )
            
            await send_message(text=form.data)
            
            try:
                db.session.add(order)
                db.session.commit()

                # send the order to the rider   
                await send_message(chat_id="2082809928",
                                   text=
                                   f"New Order:\n"
                    f"Name: {order.user}\n"
                    f"Phone: {order.phone}\n"
                    f"Location: {order.location}\n"
                    f"Order: {order.order}\n"
                    f"Notes: {order.notes}")

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





@app.route('/cancel_order/<int:order_id>', methods=['POST'])
def cancel_order(order_id):
    order = Order.query.get_or_404(order_id)
    
    if order.status != 'Cancelled':
        cancel_reason = request.form.get('cancel_reason', None)
        order.status = 'Cancelled'
        order.cancel_reason = cancel_reason 
        print('----------')
        print(cancel_reason)
        db.session.commit()
        return redirect(url_for('details'))
    else:
        return redirect(url_for('details'))


@app.route('/update_order_status/<int:id>/<string:status>', methods=['POST', 'GET'])
def update_order_status(id,status):
    print("id:",id)
    print("status:",status)
    try:
        order= Order.query.get_or_404(id)
        print("order:",order)
        order.status=status
        db.session.commit()
        print("order.status:",order.status)
    except Exception as e:
        print(e)
        print("status:",order.status)
    return redirect (url_for('motordriver'))
        



@app.route('/motordriver', methods=['GET', 'POST'])
def motordriver():
    user = Order.query.order_by(Order.id.desc()).all()
    return render_template('motor_delivery.html', user=user)



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