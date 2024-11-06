from flask import Flask, render_template
# from flask_session import Session
app = Flask(__name__,template_folder="templates",static_url_path="/static")
# Session(app)
# app.config['SECRET_KEY'] = 'supersecreto'
# app.config['SESSION_TYPE'] = 'filesystem'
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/logReg")
def iniReg():
    return render_template("logReg.html")

@app.route("/inicioSesion")
def inicioSesion():
    return render_template("login.html")

@app.route("/registrarse")
def registrarse():
    return render_template("register.html")
if __name__ == '__main__':
    app.run(debug=True)
