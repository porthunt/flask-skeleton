from flask import Blueprint


admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin.route('/dashboard/')
def dashboard():
    return 'admin dashboard'

@admin.route('/stats/')
def stats():
    return 'admin stats'
