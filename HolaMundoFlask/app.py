from flask import Flask, request, render_template, url_for, abort, jsonify, session
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = 'Mi_llave_secret'


@app.route("/")
def hello_world():
    if 'username' in session:
        return f'El usuario ya ha hecho loggin {session["username"]}'
    return 'no ha hecho loggin'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Omitimos validación de usuario y password
        usuario = request.form['username']
        # agregar el usuario a la sesión
        session['username'] = usuario
        # session['username'] = request.form['usuario']
        return redirect(url_for('hello_world'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('hello_world'))


@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f'Saludos {nombre.upper()}'


@app.route("/edad/<int:edad>")
def mostrar_edad(edad):
    return f'Tu edad es: {edad + 1}'


@app.route("/mostrar/<nombre>", methods=['GET', 'POST'])
def mostrar_nombre(nombre):
    return render_template('mostrar.html', nombre=nombre)


@app.route("/redireccionar")
def redireccionar():
    return redirect(url_for('mostrar_nombre', nombre='Danny'))


@app.route('/salir')
def salir():
    return abort(404)


# con el metodo abort salimos de la navegacion
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404


@app.route('/api/mostrar/<nombre>', methods=['GET', 'POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)
