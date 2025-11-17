from flask import Flask, render_template
from app.routes.users import setup_routes


app = Flask(__name__,template_folder='app/templates')
setup_routes(app)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/register-form")
def register_form():
    return render_template("register.html")

@app.route("/login-form")
def login_form():
    return render_template("login.html")

@app.route("/forgot-form")
def forgot_form():
    return render_template("forgot_password.html")

@app.route("/reset-form")
def reset_form():
    return render_template("reset_password.html")

if __name__ == "__main__":
    app.run(debug=True)