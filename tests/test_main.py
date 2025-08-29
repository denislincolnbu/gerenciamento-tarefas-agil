import pytest
from src.main import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa, tarefas_db, Status

def setup_function():
    tarefas_db.clear()

def test_criar_tarefa():
    criar_tarefa("Teste de Criação", "Descrição do teste.")
    assert len(tarefas_db) == 1
    assert tarefas_db[0].titulo == "Teste de Criação"
    assert tarefas_db[0].descricao == "Descrição do teste."
    assert tarefas_db[0].status == Status.A_FAZER

def test_atualizar_tarefa():
    criar_tarefa("Tarefa a Atualizar", "Descrição antiga.")
    atualizar_tarefa(1, novo_status="EM_PROGRESSO")
    assert tarefas_db[0].status == Status.EM_PROGRESSO

def test_status_invalido():
    criar_tarefa("Teste de Status Inválido", "Tarefa para teste.")
    atualizar_tarefa(1, novo_status="INVALIDO")
    assert tarefas_db[0].status == Status.A_FAZER

def test_excluir_tarefa():
    criar_tarefa("Tarefa a Excluir", "Descrição qualquer.")
    excluir_tarefa(1)
    assert len(tarefas_db) == 0
