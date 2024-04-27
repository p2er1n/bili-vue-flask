from flask import Flask, redirect, url_for, Blueprint
from . import api

app = Flask(__name__, static_url_path='')
bp = Blueprint("api", __name__, url_prefix="/api")

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

api.register_api(bp)
app.register_blueprint(bp)

