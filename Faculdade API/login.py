from flask import Flask, request, jsonify, render_template, Blueprint

login_bp = Blueprint('login', __name__)

@login_bp.route('/')
def index():
    return render_template('login.html')