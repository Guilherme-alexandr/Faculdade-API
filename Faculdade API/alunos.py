from flask import Flask, request, jsonify, render_template, Blueprint

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/')
def alunos():
    return render_template('alunos.html')