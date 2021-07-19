from flask import Flask
from config import Config  # este es el modulo de configuracion donde se guardan las claves
from flask_sqlalchemy import SQLAlchemy  # Importa el modulo que maneja las bases de datos
from flask_migrate import Migrate  # modulo que maneja los cambios en la base de datos
from flask_login import LoginManager  # modulo que maneja las sesiones de usuario
app = Flask(__name__)
app.config.from_object(Config)  # se asigna la clave secreta
db = SQLAlchemy(app)  # instancia la base de datos usando la app
migrate = Migrate(app, db)  # instancia la app y la base de datos para hacer migraciones (cambios en db)
login = LoginManager(app)  # instancia la app para controlar el login de usuarios
login.login_view = 'login'  #  esta funcion proteje paginas PARA NO SER VISTAS POR USUARIOS NO REGISTRADOS y los redirije a la pagina login
login.login_message_category = 'warning'  # esta funcion da formato a las categorias boostrap de los mensajes de usuario no registrados
from app import routes, models
