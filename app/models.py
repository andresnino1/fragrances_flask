from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin  # esta es la clase base que maneja el login

# =======================================================================================================
# =======================================================================================================
# =======================================================================================================

# En esta clase se define la tabla de la base de datos donde se guardaran los usuarios
# la clase base UserMixin hace que el modelo User sea compatible con el Login

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)  # index en true para optimizar la busqueda por username
    email = db.Column(db.String(120), index=True, unique=True)  # index en true para optimizar la busqueda por email
    password_hash = db.Column(db.String(128))
    # para encontrar facilmente el usuario de un comentario y los comentarios hechos por el usuario
    # esto creara la lista de comentarios del usuario
    # backref agrega un atributo autor a cada comentario -- se puede ponder comment.author
    # lazy crea los comentarios como una query o consulta en vez de una lista de comentarios y con esto se pueden agregar
    # filtros o nuevas opciones a la consulta.
    comments = db.relationship('Comment', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)  # para imprimir la clase en la consola de python y poder verlo claramente

    # en esta parte del codigo se crea una funcion para generar el password encriptado
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # en esta funcion se verifica el password con el password encriptado
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)  # retorna True o False si el password es correcto


# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================
# Esta clase toma el id y retorna el objeto User, esto es para el login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))  # hace una consulta y retorna el ID del usuario logueado


# ===================================================================================================================
# ===================================================================================================================
# ===================================================================================================================
# En esta clase se define la tabla de la base de datos donde se guardaran las fragrancias


class Fragrance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fragrance_code = db.Column(db.Integer, unique=True)
    essential_club = db.Column(db.Boolean)
    vigente = db.Column(db.Boolean)
    application = db.Column(db.String(100))
    commercial_name = db.Column(db.String(100))
    box = db.Column(db.Integer)
    cost_kilo_us = db.Column(db.Float)
    selling_price_aud = db.Column(db.Float)
    first_family = db.Column(db.String(100))
    second_family = db.Column(db.String(100))
    third_family = db.Column(db.String(100))
    market_type = db.Column(db.String(100))
    nota_salida = db.Column(db.String(100))
    nota_cuerpo = db.Column(db.String(100))
    nota_fondo = db.Column(db.String(100))
    expiry_date = db.Column(db.Date)
    sample_size = db.Column(db.Float)
    technology = db.Column(db.String(100))
    collection_prom = db.Column(db.String(100))
    shortlisted = db.Column(db.Boolean)
    won_selling = db.Column(db.Boolean)
    natural_extracts = db.Column(db.String(100))
    allergen = db.Column(db.Float)
    natural_percentage = db.Column(db.Boolean)
    natural_derived = db.Column(db.Boolean)
    ecocert = db.Column(db.Boolean)
    bio_degradable = db.Column(db.Boolean)
    dangerous_good = db.Column(db.Boolean)
    ai = db.Column(db.Boolean)

    def __repr__(self):
        return '<Fragrance {}>'.format(self.commercial_name)  # para imprimir la clase en la consola de python y poder verlo claramente

# ====================================================================================================================
# ====================================================================================================================
# ====================================================================================================================
# En esta clase de define la tabla de la base de datos donde se guardan los comentarios de los usuarios para cada fragrancia


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # foreignkey debe ser el nombre del modelo con punto id
    fragrance_id = db.Column(db.Integer, db.ForeignKey('fragrance.id'))  # foreignkey debe ser el nombre del modelo con punto id
    comment = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)  # fecha y hora del comentario

    def __repr__(self):
        return '<Comment {}>'.format(self.comment)  # para imprimir la clase en la consola de python y poder verlo claramente
