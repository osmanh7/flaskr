from flask import Flask, render_template

#Crear una instancia de Flask
app = Flask(__name__)

#Crear un decorador de ruta
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

#Crear paginas de error personalizadas

#URL invalida
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Error interno del servidor
@app.errorhandler(500)
def error_server(e):
    return render_template("500.html"), 500