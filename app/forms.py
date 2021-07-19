from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, DateField
from wtforms.validators import DataRequired, Email, Length


# en esta clase de define el formulario de Login usuarios registrados


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

# en esta clase se define el formulario para agregar nuevos usuarios


class AddNewUser(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Add User')

# en esta clase de define el fomulario de ingreso de nuevas fragrancias


class AddNewFragrance(FlaskForm):
    fragrance_code = StringField('Fragrance Code', validators=[DataRequired()])
    essential_club = BooleanField('Essential Club')
    vigente = BooleanField('Vigente')
    application = StringField('Application')  # este campo es many to many es como un tag
    commercial_name = StringField('Commercial Name')
    box = BooleanField('Box')
    cost_kilo_us = DecimalField('Cost Kilo Us')
    selling_prices_aud = DecimalField('Selling Price')
    first_family = StringField('First Family')  # este campo es many to many es como un tag
    second_family = StringField('Second Family')  # este campo es many to many es como un tag
    third_family = StringField('Third Family')  # este campo es many to many es como un tag
    market_type = StringField('Market Type')  # este campo es many to many es como un tag
    nota_salida = StringField('Nota Salida')  # este campo es many to many es como un tag
    nota_cuerpo = StringField('Nota Cuerpo')  # este campo es many to many es como un tag
    nota_fondo = StringField('Nota Fondo')  # este campo es many to many es como un tag
    expiry_date = DateField('Expiry Date')
    sample_size = DecimalField('Sample Size')
    technology = StringField('Technology')  # este campo es many to many es como un tag
    collection_prom = StringField('Collection')  # este campo es many to many es como un tag
    shortlisted = BooleanField('Shortlisted')
    won_selling = BooleanField('Won Selling')
    natural_extracts = StringField('Natural Extracts')  # este campo es many to many es como un tag
    allergen = DecimalField('Allergen')
    natural_percentage = BooleanField('Natural Percentage')
    natural_derived = BooleanField('Natural Derived')
    ecocert = BooleanField('Ecocert')
    bio_degradable = BooleanField('Bio Degradable')
    dangerous_good = BooleanField('Dangerous Good')
    ai = BooleanField('Ai')
