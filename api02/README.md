
---

# API02 - Catálogo de Filmes (FastAPI + melhorias)

Esta é a segunda versão da API, com melhorias em relação à api01. Também roda em **FastAPI** e está containerizada com **Docker**.

---

## 🚀 Comandos Docker utilizados

### 1. Construir a imagem
No terminal do VScode:
docker build -t api02-filmes .

👉 Cria uma imagem Docker chamada api02-filmes

2. Rodar o container
docker run -d -p 8001:8000 api02-filmes

👉 Executa a API em segundo plano, mapeando a porta 8000 do container para a porta 8001 da máquina local.
Assim, você acessa a API em: http://localhost:8001 (localhost).

3. Usar com Docker Compose
Se estiver usando o docker-compose.yml na raiz do projeto, para unificar os processos:
docker-compose up --build

👉 Sobe todos os serviços (API01, API02 e frontend) de uma vez, em vez de precisar dar run no frontend e no backend separadamente


📂 Estrutura
- main.py → código principal da API
- requirements.txt → dependências Python
- Dockerfile → instruções para construir a imagem



---
