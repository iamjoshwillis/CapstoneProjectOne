from wtforms import SelectField, StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, DataRequired

class UserSignUpForm(FlaskForm):
    """Form for adding new user"""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    image_url = StringField('Profile Picture (Optional)')
    home_planet = SelectField('Home Planet', validators=[DataRequired()], coerce=int)

class LoginForm(FlaskForm):
    """Form to Login"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class BookTravelForm(FlaskForm):
    departing_planet = SelectField('Departing Planet', validators=[DataRequired()], coerce=int)
    arriving_planet = SelectField('Where To?', validators=[DataRequired()], coerce=int)
