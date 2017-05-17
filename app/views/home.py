from flask import Blueprint, render_template
from settings import LOGIN_URL, LOGOUT_URL


home = Blueprint('home', __name__)

@home.route('/')
def index():
    return 'index'

@home.route(LOGIN_URL, methods=['GET', 'POST'])
def login():
    return 'login'

@home.route(LOGOUT_URL, methods=['GET'])
def logout():
    return 'logout'
