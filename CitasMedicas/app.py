from flask import Flask, render_template, request

from flask_session import Session
from controllers.loginYRegister import LoginYRegistro
app = Flask(__name__,template_folder="templates",static_url_path="/static")
Session(app)
app.config['SECRET_KEY'] = 'supersecreto'
app.config['SESSION_TYPE'] = 'filesystem'
loginRegister_controller = LoginYRegistro()
@app.route('/')
def index():
    return render_template("index/index.html")
# ? Ruta para la redirección a iniciar o registrarse
@app.route("/logReg")
def logReg():
    return render_template("index/logReg.html")

# ? Ruta inicio Sesión y recopilación de los datos para comprobarlo en la base de datos
@app.route("/inicioSesion")
def inicioSesion():
    return render_template("index/login.html")

# * Ruta formulario inicioSesion
@app.route("/loginUser", methods=['GET'] )
def iniciarSesion():
    usuario = request.args.get('usuario')
    contrasenia = request.args.get('contrasenia')
    loginRegister_controller.login(usuario,contrasenia)
# ? Ruta registrarse y recopilación de datos para registrarlos en la base de datos
@app.route("/registrarse")
def registrarse():
    return render_template("index/register.html")

# * Ruta formulario registro usuario
@app.route("/createUser", methods=['GET'])
def registrarse():
    nombre = request.args.get('nombre')
    apellidos = request.args.get('apellidos')
    dni = request.args.get('dni')
    fechaNacimiento = request.args.get('fechaNacimiento')
    usuario = request.args.get('usuario')
    contrasenia = request.args.get('contrasenia')
    contrasenia2 = request.args.get('contrasenia2')
    loginRegister_controller.register(nombre,apellidos, dni, fechaNacimiento, usuario, contrasenia, contrasenia2)
    
# ? Ruta recuperar contraseña y recopilación de datos para enviar correo de recuperación
@app.route("/lostpass")
def lostPass():
    return render_template("index/lostPassword.html")

# * Ruta de recuperación de cuenta
@app.route("/lostPassword", methods=['GET'])
def lostPass():
    recuperar = request.args.get('recuperar')

if __name__ == '__main__':
    app.run(debug=True)
