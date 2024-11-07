from flask import Flask, render_template
# from flask_session import Session
app = Flask(__name__,template_folder="templates",static_url_path="/static")
# Session(app)
# app.config['SECRET_KEY'] = 'supersecreto'
# app.config['SESSION_TYPE'] = 'filesystem'
@app.route('/')
def index():
    return render_template("index/index.html")

@app.route("/logReg")
def logReg():
    return render_template("index/logReg.html")

@app.route("/inicioSesion")
def inicioSesion():
    return render_template("index/login.html")

@app.route("/registrarse")
def registrarse():
    return render_template("index/register.html")

@app.route("/lostpass")
def lostPass():
    return render_template("index/lostPassword.html")
if __name__ == '__main__':
    app.run(debug=True)
