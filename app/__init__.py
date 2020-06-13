from flask import Flask
from .views import home, admin


app = Flask(__name__)
app.config.from_object("settings")

app.register_blueprint(home)
app.register_blueprint(admin)
