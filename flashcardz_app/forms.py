#from msilib.schema import RadioButton
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, IntegerField
from wtforms.validators import DataRequired,Email,EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators = [DataRequired()])
    password2 = PasswordField('Confirm Password', validators = [DataRequired(),EqualTo('password1')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CreateDecksForm(FlaskForm):
    deck_name = StringField('Name of Deck', validators=[DataRequired()])
    submit = SubmitField('Create Deck')

class AddCardForm(FlaskForm):
    front = StringField('Front of Card', validators=[DataRequired()])
    back = StringField('Back of Card', validators=[DataRequired()])
    submit = SubmitField('Create Card')
