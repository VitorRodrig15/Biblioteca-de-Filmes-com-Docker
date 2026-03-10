# Usa Node como imagem base
FROM python:3.9

# Define diretório de trabalho dentro do container
WORKDIR /api

# Copia os arquivos de dependência primeiro
COPY . .

# Instala dependências
RUN pip install fastapi uvicorn

# Comando para iniciar o servidor de desenvolvimento e suas funções de aplicação, porta do localhost
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

