from flask import Flask, render_template, request , jsonify, session
from flask_session import Session
from controllers.loginYRegister import LoginYRegistro
from database.migrations import migraciones
app = Flask(__name__,template_folder="templates",static_url_path="/static")
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'supersecreto'
Session(app)


loginRegister_controller = LoginYRegistro()
migraciones()
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
def ini():
    usuario = request.args.get('usuario')
    contrasenia = request.args.get('contrasenia')
    resultado = loginRegister_controller.login(usuario,contrasenia)
    if resultado['id'] != False:
        session['user']=resultado['id']
        return jsonify({'estado':True})
    else:
        return jsonify({'estado':False})
# ? Ruta registrarse y recopilación de datos para registrarlos en la base de datos
@app.route("/registrarse")
def registrarse():
    return render_template("index/register.html")

# * Ruta formulario registro usuario
@app.route("/createUser", methods=['GET'])
def regi():
    nombre = request.args.get('nombre')
    apellidos = request.args.get('apellidos')
    dni = request.args.get('dni')
    fechaNacimiento = request.args.get('fechaNacimiento')
    usuario = request.args.get('usuario')
    contrasenia = request.args.get('contrasenia')
    resultado = loginRegister_controller.register(nombre,apellidos, dni, fechaNacimiento, usuario, contrasenia)
    if resultado:
        return jsonify(resultado)
    else:
        return jsonify("Fallo","No se ha podido ")
    
# ? Ruta recuperar contraseña y recopilación de datos para enviar correo de recuperación
@app.route("/lostpass")
def contraseniaPerdida():
    return render_template("index/lostPassword.html")

# * Ruta de recuperación de cuenta
@app.route("/lostPassword", methods=['GET'])
def lostPass():
    recuperar = request.args.get('recuperar')
    loginRegister_controller.recuperar(recuperar)


@app.route("/home")
def home():
    return render_template("home/home.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000, debug=True)
    
