from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


# ===================================================================================================== #
# ===================================================================================================== #
# ============================= FORMULARIO DE LOGIN USUARIOS REGISTRADOS ============================== #
# ===================================================================================================== #
# ===================================================================================================== #


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# ===================================================================================================== #
# ===================================================================================================== #
# ================================== FORMULARIO DE REGISTRO NUEVOS USUARIOS =========================== #
# ===================================================================================================== #
# ===================================================================================================== #


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    # este metodo valida el formulario de registro para que el usuario registrado y email sean unicos
    # Estos son metodos que proporciona WTF para validar, se usa la palabra validate_ seguida del nombre
    # del cambo que se quiere validar.

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email.')


# ===================================================================================================== #
# ===================================================================================================== #
# =========================== FORMULARIO DE INGRESO DE NUEVAS FRAGRANCIASS ============================ #
# ===================================================================================================== #
# ===================================================================================================== #


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
