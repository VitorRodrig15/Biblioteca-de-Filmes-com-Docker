# Frontend - Biblioteca de Filmes (React)

Este é o frontend da aplicação, feito em **React** e containerizado com **Docker**.  
Ele consome as APIs (`api01` e `api02`) e exibe a interface web para o catálogo de filmes.

---

## 🚀 Comandos Docker utilizados

### 1. Construir a imagem
No terminal:
docker build -t frontend-filmes .

👉 Cria uma imagem Docker chamada frontend-filmes a partir do Dockerfile presente nesta pasta.

2. Rodar o container
docker run -d -p 3000:3000 frontend-filmes

👉 Executa o frontend em segundo plano (-d), mapeando a porta 3000 do container para a porta 3000 da máquina local.
Assim, você acessa a interface em: http://localhost:3000.

4. Usar com Docker Compose
Se estiver usando o docker-compose.yml na raiz do projeto:
docker-compose up --build

👉 Sobe todos os serviços (API01, API02 e frontend) de uma vez, já integrados

📂 Estrutura
- src/ → código React (componentes, páginas, estilos)
- package.json → dependências e scripts do projeto
- Dockerfile → instruções para construir a imagem do frontend


💡 Objetivo
O frontend conecta com as APIs e exibe os filmes de forma simples e interativa.
É a camada visual do sistema, permitindo que o usuário navegue e veja os dados fornecidos pelo backend.

