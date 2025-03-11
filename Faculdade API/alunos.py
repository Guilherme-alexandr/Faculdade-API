from flask import Flask, request, jsonify, render_template, Blueprint

dici = {
    "alunos":[
        {
            "id":1,
            "nome":"Lucas Silva",
            "idade": "19"            
        }
    ],

    "professor":[
        {
            "id":1,
            "nome":"Marcos"
        }
    ],

     "turma":[
        {
            "id":1,
            "nome":"API"
        }
    ],
}

alunos_bp = Blueprint('alunos', __name__)

@alunos_bp.route('/')
def alunos():
    return render_template('alunos.html')



@alunos_bp.route('/alunos/dici', methods=['GET'])
def getAluno():
    dados = dici["alunos"]
    print(dados)
    return jsonify(dados)

@alunos_bp.route('/professores/dici', methods=['GET'])
def getProfessor():
    dados = dici["professor"]
    print(dados)
    return jsonify(dados)

@alunos_bp.route('/alunos',methods=['POST'])
def createAluno():
    dados = request.json
    dici['alunos'].append(dados)
    return jsonify(dados)



@alunos_bp.route("/alunos/<int:idAluno>", methods=['PUT'])
def updateAlunos(idAluno):
    alunos = dici["alunos"]
    for aluno in alunos:
        if aluno['id'] == idAluno:
            dados = request.json
            aluno["id"] = dados['id']
            aluno['nome'] = dados['nome']
            return jsonify(dados)
        else:
            return jsonify("aluno nao encontrado")


