from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Professor(Base):
    __tablename__ = 'professores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    idade = Column(Integer(3), nullable=False)
    materia =  Column(String(100))
    observacoes = Column(String(100))
    
class Turma(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True)
    descricao = Column(String(100), nullable=False)
    professor_id = Column(Integer, ForeignKey('professores.id'))
    ativo = Column(bool)

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    idade = Column(Integer(3), nullable=False)
    turma_id = Column(Integer, ForeignKey('turmas.id'))
    data_nascimento =  Column(Integer(8), nullable=False)
    
