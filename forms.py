from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, DateField, FloatField,SubmitField, BooleanField, SelectField, IntegerField, RadioField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from wtforms.widgets import TextArea

class Delivery(FlaskForm):
    pickup = StringField('Pick Up')
    name = StringField('Name')
    
    dropoff = StringField('Drop Off')
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])

    picture = StringField('Picture')

    description = StringField('Description',widget=TextArea())
    notes = StringField('Notes', widget=TextArea())

    location = StringField('Location', widget=TextArea(), validators=[DataRequired()])
    submit = SubmitField('Proceed')