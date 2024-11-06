import os
from flask import Flask,redirect,url_for,render_template,request
from forms import Delivery
from utils import send_message

app=Flask(__name__)

app.config['SECRET_KEY'] = 'c2ba24216b13s5e0c676d8b8021579fde'
app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DELIVERY_DB_URL')

@app.route('/',methods=['GET','POST'])
async def details(): 
    form = Delivery()
    if request.method == 'POST':
        # create an order and send broadcast
        if form.validate_on_submit():
            print(form.data)

            await send_message(text=form.data)

            return redirect(url_for('order_details'))
        else:
            print(form.errors)
    return render_template('index.html', form=form)

# 

@app.route('/order_details', methods=['GET', 'POST'])
def order_details():
    return render_template('order_details.html')
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, host='0.0.0.0', debug=True)