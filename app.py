import os
from flask import Flask,redirect,url_for,render_template,request
from forms import Delivery

app=Flask(__name__)

app.config['SECRET_KEY'] = 'c2ba24216b13s5e0c676d8b8021579fde'
# app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DELIVERY_DB_URL')

@app.route('/',methods=['GET','POST'])
def details():
    form = Delivery()
    if request.method == 'POST':
        
        return render_template('index.html')
    return render_template('index.html', form=form)

# 

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, host='0.0.0.0', debug=True)