from flask import Flask
from config import Config  # este es el modulo de configuracion donde se guardan las claves


app = Flask(__name__)
app.config.from_object(Config)  # se asigna la clave secreta
from app import routes
