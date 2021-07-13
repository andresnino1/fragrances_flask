from app import app  # se importa app desde el archivo __init__ que esta dentro de la carpeta app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andres'}
    fragrances = [
        {'fragrance_code': 123, 'user': {'username': 'Andres'}, 'commercial_name': 'Fragrance Good'},
        {'fragrance_code': 456, 'user': {'username': 'Roberto'}, 'commercial_name': 'Fragrance Rose'}
    ]

    return render_template('index.html', title='Fragrances - Home', user=user, fragrances=fragrances)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # aqui estoy creado el formulario de login y lo pongo en la variable form
    form = LoginForm()
    # si todos los campos estan validados correctamente dara verdadero el IF
    # para verificar que los datos estan llegando desde el formulario se envian mensajes con flash
    # los mensajes se pasaran al template base.html
    # se redirige al final a la pagina index
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)
