from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, DateField, FloatField,SubmitField, BooleanField, SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from wtforms.widgets import TextArea

class Delivery(FlaskForm):
    pickup = StringField('Pick Up', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    
    dropoff = StringField('Drop Off', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])

    picture = StringField('Picture', validators=[DataRequired()])

    description = StringField('Description',widget=TextArea(), validators=[DataRequired()])
    notes = StringField('Notes', widget=TextArea(), validators=[DataRequired()])

    location = StringField('Location', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Proceed')