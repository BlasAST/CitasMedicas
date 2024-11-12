from flask import Flask, render_template, request
# from flask_session import Session
app = Flask(__name__,template_folder="templates",static_url_path="/static")
# Session(app)
# app.config['SECRET_KEY'] = 'supersecreto'
# app.config['SESSION_TYPE'] = 'filesystem'
@app.route('/')
def index():
    return render_template("index/index.html")
# * Ruta para la redirección a iniciar o registrarse
@app.route("/logReg")
def logReg():
    return render_template("index/logReg.html")
# * Ruta inicio Sesión y recopilación de los datos para comprobarlo en la base de datos
@app.route("/inicioSesion", methods=['GET'] )
def inicioSesion():
    usuario = request.args.get('usuario')
    contrasenia = request.args.get('contrasenia')
    return render_template("index/login.html")
# * Ruta registrarse y recopilación de datos para registrarlos en la base de datos
@app.route("/registrarse", methods=['GET'])
def registrarse():
    nombre = request.args.get('nombre')
    apellidos = request.args.get('apellidos')
    dni = request.args.get('dni')
    fechaNacimiento = request.args.get('fechaNacimiento')
    usuario = request.args.get('usuario')
    contrasenia = request.args.get('contrasenia')
    contrasenia2 = request.args.get('contrasenia2')

    return render_template("index/register.html")
# * Ruta recuperar contraseña y recopilación de datos para enviar correo de recuperación
@app.route("/lostpass", methods=['GET'])
def lostPass():
    recuperar = request.args.get('recuperar')
    return render_template("index/lostPassword.html")
if __name__ == '__main__':
    app.run(debug=True)
    
