# Arquivo: src/main.py

from models.tarefa import Tarefa, Status
from datetime import datetime

# Simulação de um banco de dados
tarefas_db = []
id_contador = 1

def criar_tarefa(titulo, descricao):
    """
    Cria uma nova tarefa e a adiciona ao 'banco de dados'.
    """
    global id_contador
    nova_tarefa = Tarefa(titulo, descricao)
    nova_tarefa.idTarefa = id_contador
    tarefas_db.append(nova_tarefa)
    id_contador += 1
    print(f"Tarefa '{nova_tarefa.titulo}' criada com sucesso! ID: {nova_tarefa.idTarefa}")

def listar_tarefas():
    """
    Lista todas as tarefas existentes no 'banco de dados'.
    """
    if not tarefas_db:
        print("Nenhuma tarefa encontrada.")
        return

    print("\n--- Lista de Tarefas ---")
    for tarefa in tarefas_db:
        print(f"ID: {tarefa.idTarefa}, Título: {tarefa.titulo}, Status: {tarefa.status.value}, Criada em: {tarefa.dataCriacao.strftime('%d/%m/%Y %H:%M')}")
    print("------------------------")

def atualizar_tarefa(id_tarefa, novo_titulo=None, nova_descricao=None, novo_status=None):
    """
    Atualiza uma tarefa existente no 'banco de dados'.
    """
    for tarefa in tarefas_db:
        if tarefa.idTarefa == id_tarefa:
            if novo_titulo:
                tarefa.titulo = novo_titulo
            if nova_descricao:
                tarefa.descricao = nova_descricao
            if novo_status:
                try:
                    tarefa.status = Status[novo_status.upper()]
                except KeyError:
                    print(f"Status '{novo_status}' inválido. Por favor, use: A_FAZER, EM_PROGRESSO ou CONCLUIDO.")
                    return
            
            # Atualiza a data de conclusão se o status for CONCLUIDO
            if tarefa.status == Status.CONCLUIDO and not tarefa.dataConclusao:
                tarefa.dataConclusao = datetime.now()

            print(f"Tarefa com ID {id_tarefa} atualizada com sucesso!")
            return

    print(f"Erro: Tarefa com ID {id_tarefa} não encontrada.")

def excluir_tarefa(id_tarefa):
    """
    Exclui uma tarefa do 'banco de dados'.
    """
    global tarefas_db
    tarefas_db = [tarefa for tarefa in tarefas_db if tarefa.idTarefa != id_tarefa]
    print(f"Tarefa com ID {id_tarefa} excluída com sucesso!")

# --- Menu e Exemplo de Uso ---

def menu():
    print("\n--- Menu do Sistema de Tarefas ---")
    print("1. Criar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Atualizar uma tarefa")
    print("4. Excluir uma tarefa")
    print("5. Sair")
    
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                titulo = input("Digite o título da tarefa: ")
                descricao = input("Digite a descrição da tarefa: ")
                criar_tarefa(titulo, descricao)
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                id_tarefa = int(input("Digite o ID da tarefa para atualizar: "))
                novo_titulo = input("Novo título (deixe em branco para não alterar): ")
                nova_descricao = input("Nova descrição (deixe em branco para não alterar): ")
                novo_status = input("Novo status (A_FAZER, EM_PROGRESSO, CONCLUIDO - deixe em branco para não alterar): ")
                atualizar_tarefa(id_tarefa, novo_titulo or None, nova_descricao or None, novo_status or None)
            elif opcao == 4:
                id_tarefa = int(input("Digite o ID da tarefa para excluir: "))
                excluir_tarefa(id_tarefa)
            elif opcao == 5:
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

# Executa o menu
if __name__ == "__main__":
    menu()