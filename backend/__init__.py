from flask import Flask, redirect, url_for

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

