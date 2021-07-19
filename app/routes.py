from app import app  # se importa app desde el archivo __init__ que esta dentro de la carpeta app
from werkzeug.urls import url_parse
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm
from app.models import User
from flask_login import login_user, current_user, logout_user, login_required


#  ==================================================================================================================
#  ============================================HOME PAGE=============================================================
#  ==================================================================================================================


@app.route('/')
@app.route('/index')
@login_required  # este decorador proteje la pagina index para ser vista solo por usuarios registrados
def index():
    fragrances = [
        {'fragrance_code': 123, 'user': {'username': 'Andres'}, 'commercial_name': 'Fragrance Good'},
        {'fragrance_code': 456, 'user': {'username': 'Roberto'}, 'commercial_name': 'Fragrance Rose'}
    ]

    return render_template('index.html', title='Fragrances - Home', fragrances=fragrances)


#  ==================================================================================================================
#  ============================================LOGIN=================================================================
#  ==================================================================================================================

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))  # si el usuario intenta logearse de nuevo se redirecciona al idex
    # aqui estoy creado el formulario de login y lo pongo en la variable form
    form = LoginForm()
    # si todos los campos estan validados correctamente dara verdadero el IF

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        # se consulta por el usuario que se ingresa en el formulario
        # pregunta si el usuario NO esta en la base de datos O el pass fue invalido
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password','danger')  # envia mensaje de error
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)  # esta funcion hace que el usuario haga login y se recuerde en la web
        next_page = request.args.get('next')  # esta variable guarda el url que intenta acceder el usuario antes del login
        # se pregunta si NO existe una pagina next_page o si el netloc (dominio) esta vacio
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


#  ==================================================================================================================
#  ============================================LOGOUT================================================================
#  ==================================================================================================================


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


#  ==================================================================================================================
#  ============================================ADD FRAGRANCES =======================================================
#  ==================================================================================================================


@app.route('/addfragrance')
@login_required
def add_fragrance():
    return render_template('add_fragrance.html', title='Add Fragrance')

