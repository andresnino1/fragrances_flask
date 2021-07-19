from app import app, db
from app.models import User, Comment, Fragrance


# esta parte del codigo importa la base de datos y los modelos para poder usarlo facilmente
# al activar el flask shell en la linea de comandos
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Comment': Comment, 'Fragrance': Fragrance}
