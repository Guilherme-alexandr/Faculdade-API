from flask import Flask, request, jsonify, render_template, Blueprint

turmas_bp = Blueprint('turmas', __name__)

@turmas_bp.route('/')
def turmas():
    return render_template('turmas.html')