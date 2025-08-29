# Arquivo: tests/test_main.py

import pytest
from src.main import criar_tarefa, listar_tarefas, atualizar_tarefa, excluir_tarefa
from src.models.tarefa import Tarefa, Status

# Configura um banco de dados de teste (um novo para cada teste)
@pytest.fixture(autouse=True)
def setup_teardown():
    global tarefas_db, id_contador
    tarefas_db = []
    id_contador = 1
    yield

def test_criar_tarefa():
    """Testa se a função de criar tarefa funciona corretamente."""
    criar_tarefa("Teste de Criação", "Descrição do teste.")
    assert len(tarefas_db) == 1
    assert tarefas_db[0].titulo == "Teste de Criação"
    assert tarefas_db[0].status == Status.A_FAZER

def test_atualizar_tarefa():
    """Testa a atualização de uma tarefa existente."""
    criar_tarefa("Tarefa a Atualizar", "Descrição antiga.")
    atualizar_tarefa(1, novo_status="EM_PROGRESSO")
    assert tarefas_db[0].status == Status.EM_PROGRESSO
    
def test_excluir_tarefa():
    """Testa se uma tarefa pode ser excluída."""
    criar_tarefa("Tarefa a Excluir", "Para ser removida.")
    excluir_tarefa(1)
    assert len(tarefas_db) == 0

def test_status_invalido():
    """Testa se a função de atualização rejeita um status inválido."""
    criar_tarefa("Teste de Status Inválido", "Tarefa para teste.")
    atualizar_tarefa(1, novo_status="INVALIDO")
    # O status deve permanecer o mesmo
    assert tarefas_db[0].status == Status.A_FAZER