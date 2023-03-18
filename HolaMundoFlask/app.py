from flask import Flask, request, render_template, url_for, abort, jsonify
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    app.logger.info(f'Entramos al path /{request.path}')
    return "<p>Hello, World!!!!</p>"

@app.route("/saludar/<nombre>")
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

@app.route("/edad/<int:edad>")
def mostrar_edad(edad):
    return f'Tu edad es: {edad+1}'
@app.route("/mostrar/<nombre>", methods=['GET','POST'])
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
@app.route('/api/mostrar/<nombre>', methods=['GET','POST'])
def mostrar_json(nombre):
    valores = {'nombre': nombre, 'metodo_http': request.method}
    return jsonify(valores)