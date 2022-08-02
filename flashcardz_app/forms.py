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
    card_count = IntegerField("Number of Cards", validators=[DataRequired()])
    submit = SubmitField('Create')

class AddCardForm(FlaskForm):
    front = StringField('Front of Card', validators=[DataRequired()])
    back = StringField('Back of Card', validators=[DataRequired()])
    submit = SubmitField('Create')

class AddAnswerForm(FlaskForm):
    yes = BooleanField("Yes")
    no = BooleanField("No")
    submit = SubmitField('Submit')