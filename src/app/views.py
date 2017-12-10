from app import app
from flask import (render_template, request, url_for, redirect, jsonify)
import json


@app.route('/')
@app.route('/index')
def index():
    return render_template("login.html")