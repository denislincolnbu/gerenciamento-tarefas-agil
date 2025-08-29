from enum import Enum
from datetime import datetime

class Status(Enum):
    A_FAZER = "A_FAZER"
    EM_PROGRESSO = "EM_PROGRESSO"
    CONCLUIDO = "CONCLUIDO"

class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao):
        self.id = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.status = Status.A_FAZER
        self.data_criacao = datetime.now()
        self.data_conclusao = None

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.status.value}"

tarefas_db = []

def criar_tarefa(titulo, descricao):
    global tarefas_db
    nova_tarefa = Tarefa(len(tarefas_db) + 1, titulo, descricao)
    tarefas_db.append(nova_tarefa)
    print(f"Tarefa '{titulo}' criada com sucesso! ID: {nova_tarefa.id}")
    return nova_tarefa

def listar_tarefas():
    global tarefas_db
    if not tarefas_db:
        print("Nenhuma tarefa encontrada.")
    for tarefa in tarefas_db:
        print(tarefa)

def atualizar_tarefa(id_tarefa, novo_titulo=None, nova_descricao=None, novo_status=None):
    global tarefas_db
    for tarefa in tarefas_db:
        if tarefa.id == id_tarefa:
            if novo_titulo:
                tarefa.titulo = novo_titulo
            if nova_descricao:
                tarefa.descricao = nova_descricao
            if novo_status:
                if novo_status in Status._member_names_:
                    tarefa.status = Status[novo_status]
                    if tarefa.status == Status.CONCLUIDO:
                        tarefa.data_conclusao = datetime.now()
                else:
                    print("Erro: Status inválido.")
            print(f"Tarefa com ID {id_tarefa} atualizada com sucesso!")
            return tarefa
    print(f"Erro: Tarefa com ID {id_tarefa} não encontrada.")
    return None

def excluir_tarefa(id_tarefa):
    global tarefas_db
    for tarefa in tarefas_db:
        if tarefa.id == id_tarefa:
            tarefas_db.remove(tarefa)
            print(f"Tarefa com ID {id_tarefa} excluída com sucesso!")
            return True
    print(f"Erro: Tarefa com ID {id_tarefa} não encontrada.")
    return False

if __name__ == "__main__":
    criar_tarefa("Implementar CRUD", "Desenvolver funções de criar, listar, atualizar e excluir tarefas.")
    criar_tarefa("Testar Sistema", "Rodar os testes unitários para validar o sistema.")
    listar_tarefas()
    atualizar_tarefa(1, novo_status="EM_PROGRESSO")
    excluir_tarefa(2)
    listar_tarefas()
