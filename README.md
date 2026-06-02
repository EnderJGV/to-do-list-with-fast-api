# to-do-list-with-fast-api
Creating um to do list com fast api
# To-Do List API

Este projeto consiste em uma API RESTful desenvolvida para o gerenciamento de tarefas (to-do list). A aplicacao foi construida utilizando o framework FastAPI, focando em performance, escalabilidade e facil manutencao atraves de uma estrutura modular.

## Arquitetura e Organizacao

O projeto utiliza uma divisao por funcionalidades (features). O arquivo principal `main.py` centraliza a configuracao da aplicacao e inclui os roteadores especificos, como o `tasks_router`, localizado em `src.features.tasks.router`.

## Requisitos para Execucao

1. Instale o gerenciador de pacotes uv em seu sistema.
2. Sincronize o ambiente e instale as dependencias:
   ```bash
   uv sync
   ```
3. Comando para iniciar o servidor:
   ```bash
   uv run uvicorn main:app --reload
   ```

## Endpoints e Como Realizar Requisicoes

Abaixo estao os detalhes dos endpoints principais e exemplos de como interagir com eles via terminal (curl).

### 1. Raiz (Boas-vindas)
Utilizado para verificar a disponibilidade da API.
* Metodo: GET
* URL: http://localhost:8000/
* Requisicao:
  ```bash
  curl -X GET http://localhost:8000/
  ```

### 2. Documentacao Automatica
O FastAPI gera automaticamente documentacoes interativas para teste:
* Swagger UI: http://localhost:8000/docs
* Redoc: http://localhost:8000/redoc

### 3. Endpoints de Tarefas
Os endpoints para criacao, listagem e edicao de tarefas estao agrupados sob o prefixo definido no roteador de tarefas. Consulte a documentacao Swagger para os esquemas de dados (JSON) aceitos.

## Referencias Tecnicas e Padroes

Para garantir a qualidade do desenvolvimento, o projeto sinaliza a utilizacao das seguintes referencias:

* Documentacao FastAPI: Guia oficial para manipulacao de rotas e dependencias.
* Padrao REST: Utilizacao correta de verbos HTTP (GET, POST, PUT, DELETE).
* PEP 8: Guia de estilo para codigo Python.
* Type Hinting: Uso de tipagem estatica do Python para maior seguranca e documentacao automatica.

---
Projeto desenvolvido para fins de estudo e gerenciamento de tarefas pessoais.
