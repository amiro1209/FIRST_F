from flask import Blueprint, render_template

templates_bp = Blueprint("templates", __name__, url_prefix="/")

@templates_bp.route('/')
def home():
    return render_template("index.html")

@templates_bp.route("/register-form")
def register_form():
    return render_template("register.html")

@templates_bp.route("/login-form")
def login_form():
    return render_template("login.html")

@templates_bp.route("/forgot-form")
def forgot_form():
    return render_template("forgot_password.html")

@templates_bp.route("/reset-form")
def reset_form():
    return render_template("reset_password.html")