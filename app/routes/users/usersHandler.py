from flask import Blueprint, request
from ..utils.register import register_util
from ..utils.login import login_utils
from ..utils.forgot_password import forgot_password_utils
from ..utils.reset_password import reset_password_utils

user_bp = Blueprint("user" ,__name__ ,url_prefix="/user")

@user_bp.route("/register" , methods=["POST"])
def register():
    name = request.form.get("name")
    phone = request.form.get("phone")
    password = request.form.get("password")

    return register_util(name,phone,password)


@user_bp.route("/login",methods=["POST"])
def login(): 
    name = request.form.get("name")
    password = request.form.get("password")

    return login_utils(name,password)


@user_bp.route("/forgot_password",methods=["POST"])
def forgot():
    phone = request.form.get("phone")
    return forgot_password_utils(phone)


@user_bp.route("/reset",methods=["POST"])
def reset():
    code = request.form.get("code")
    new_password = request.form.get("new_password")
    return reset_password_utils(code, new_password)