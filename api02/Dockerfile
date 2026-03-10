# Usa Node como imagem base
FROM node:20-alpine

# Define diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependência da subpasta frontend
COPY frontend/package*.json ./

# Instala dependências
RUN npm install --legacy-peer-deps

# Copia o restante do código da subpasta frontend
COPY frontend ./

# Expõe a porta padrão do React
EXPOSE 3000

# Comando para iniciar o servidor de desenvolvimento
CMD ["npm", "start"]