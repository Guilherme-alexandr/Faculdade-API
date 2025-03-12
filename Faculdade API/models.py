from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer(3), nullable=False)
    data_nascimento = Column(String(15), nullable=False)
    disciplina =  Column(String(100))
    salario = Column(float(6))
   
class Turma(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    turno = Column(String(15), nullable=False)
    ativo = Column(bool)

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    idade = Column(Integer(3), nullable=False)
    data_nascimento =  Column(Integer(8), nullable=False)
    nota_primeiro_semestre = Column(float(3))
    nota_segundo_semestre = Column(float(3))
    media_final = Column(float(3))
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    
