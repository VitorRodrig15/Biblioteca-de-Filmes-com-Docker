# 🎬 Biblioteca-de-Filmes-com-Docker
Um sistema simples e divertido de catálogo de filmes, com API em FastAPI e frontend em React, tudo rodando em containers com Docker.
A ideia é mostrar como integrar backend e frontend em um ambiente isolado e fácil de subir.
 
👨‍💻⚡Tecnologias usadas
- FastAPI → para criar a API de filmes
- React → para a interface web
- Docker & Docker Compose → para orquestrar os serviços
- Python e Node.js → base do backend e frontend

⚙️ Como rodar o projeto
- Clone este repositório:
git clone https://github.com/VitorRodrig15/Biblioteca-de-Filmes-com-Docker.git
cd Biblioteca-de-Filmes-com-Docker

- Suba os containers com Docker Compose:
docker-compose up --build

- Acesse:
- API → http://localhost:8000/api (localhost no navegador)
- Frontend → http://localhost:3000 (localhost no navegador)

📂 Estrutura do projeto
- api01/ → primeira versão da API em FastAPI
- api02/ → segunda versão da API (com melhorias)
- frontend/ → interface em React
- docker-compose.yml → orquestração dos serviços, fazendo iniciar uma unica parte ligando ambos as api's
- .gitignore → arquivos ignorados no Git

💡 Objetivo
Esse projeto foi feito para praticar integração de serviços com Docker e mostrar como é possível rodar backend e frontend juntos de forma simples.
É um exemplo leve, mas que pode ser expandido para algo maior.

✨ Próximos passos
- Adicionar banco de dados (PostgreSQL ou Mysql)
- Criar autenticação de usuários
- Melhorar o design do frontend
- Integração de imagens de capas de filmes
- Melhorias em interface CSS

  

  

