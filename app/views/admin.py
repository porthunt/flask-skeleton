from flask import Blueprint


admin = Blueprint("admin", __name__, url_prefix="/admin")


@admin.route("/")
def index():
    return {
        "code": 200,
        "status": "ok"
    }


@admin.route("/stats")
def stats():
    return {
        "code": 200,
        "status": "ok"
    }
