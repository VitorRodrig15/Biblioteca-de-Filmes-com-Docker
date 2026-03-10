# API01 - Catálogo de Filmes (FastAPI)

Esta é a primeira versão da API de catálogo de filmes, feita em **FastAPI** e containerizada com **Docker**.

---

## 🚀 Comandos Docker utilizados

### 1. Construir a imagem, no terminal do vscode dentro do diretório da pasta:

bash
docker build -t api01-filmes .

👉 Cria uma imagem Docker chamada api01-filmes a partir do Dockerfile presente nesta pasta.

2. Rodar o container
docker run -d -p 8000:8000 api01-filmes

👉 Executa a API em segundo plano (-d), mapeando a porta 8000 do container para a porta 8000 da máquina local.
Assim, você acessa a API em: http://localhost:8000/API (localhost).

Caso precise parar o container
docker stop <id_do_container>
👉 Interrompe a execução do container

📂 Estrutura
- main.py → código principal da API
- requirements.txt → dependências Python
- Dockerfile → instruções para construir a imagem

