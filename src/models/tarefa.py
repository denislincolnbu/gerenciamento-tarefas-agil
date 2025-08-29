# Arquivo: src/models/tarefa.py

from datetime import datetime
from enum import Enum

class Status(Enum):
    A_FAZER = "A Fazer"
    EM_PROGRESSO = "Em Progresso"
    CONCLUIDO = "Concluído"

class Tarefa:
    def __init__(self, titulo, descricao):
        self.idTarefa = None
        self.titulo = titulo
        self.descricao = descricao
        self.status = Status.A_FAZER
        self.dataCriacao = datetime.now()
        self.dataConclusao = None