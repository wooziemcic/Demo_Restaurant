from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return render_template('login.html', title="Login")

@auth_bp.route('/signup')
def signup():
    return render_template('signup.html', title="Signup")
