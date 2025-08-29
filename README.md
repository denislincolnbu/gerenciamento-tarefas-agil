# Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

Este repositório é um projeto de portfólio desenvolvido para a disciplina de Engenharia de Software da **UniFECAF**. O projeto simula a criação de um sistema de gerenciamento de tarefas para a empresa fictícia TechFlow Solutions, que atende uma startup de logística.

O objetivo é aplicar os conceitos de metodologias ágeis e demonstrar habilidades práticas em planejamento, desenvolvimento e gestão de software, utilizando as ferramentas do GitHub.

---

## 📌 Contexto e Objetivos

O projeto se baseia na criação de um sistema de gerenciamento de tarefas utilizando metodologias ágeis. Como desenvolvedor e gestor, meu papel foi planejar, criar e gerenciar um repositório no GitHub para simular o desenvolvimento do sistema, desde a organização do código até a implementação de funcionalidades básicas e controle de qualidade.

## 📊 Metodologia Adotada

A metodologia ágil adotada foi o **Kanban**. O fluxo de trabalho foi gerenciado na aba "Projects" do GitHub, com as colunas:

* **A Fazer:** Tarefas a serem iniciadas.
* **Em Progresso:** Tarefas em desenvolvimento.
* **Concluído:** Tarefas finalizadas.

## ⚙️ Funcionalidades Implementadas

O sistema básico implementa as funcionalidades essenciais de um CRUD (Create, Read, Update, Delete) para gerenciamento de tarefas, seguindo a modelagem de classes definida.

* **Criação de Tarefas:** Adiciona uma nova tarefa com título e descrição.
* **Visualização de Tarefas:** Lista todas as tarefas existentes.
* **Atualização de Tarefas:** Permite alterar o título, a descrição e o status de uma tarefa.
* **Exclusão de Tarefas:** Remove uma tarefa do sistema.

## ✅ Controle de Qualidade

Para garantir a confiabilidade do software, foi configurado um pipeline básico de controle de qualidade usando **GitHub Actions**. O pipeline executa testes automatizados a cada novo commit, verificando se as funcionalidades do CRUD estão operando conforme o esperado.

## 🚀 Como Executar o Projeto

Para rodar o projeto localmente, siga os passos abaixo:

1.  **Clone o Repositório:**
    `git clone https://github.com/seu-usuario/gerenciamento-tarefas-agil.git`
2.  **Acesse a Pasta:**
    `cd gerenciamento-tarefas-agil`
3.  **Instale as Dependências:**
    O projeto usa a biblioteca `pytest`. Certifique-se de que o Python está instalado e use o seguinte comando:
    `pip install pytest`
4.  **Execute o Código:**
    `python src/main.py`
5.  **Execute os Testes:**
    `pytest`

---

## 🎨 Modelagem e Diagramas

A modelagem de requisitos e os diagramas UML foram criados utilizando a ferramenta `draw.io`, conforme exigido na tarefa.

* **Diagrama de Casos de Uso:** Representa a interação do usuário com o sistema.
* **Diagrama de Classes:** Descreve a estrutura e os atributos das classes do projeto.