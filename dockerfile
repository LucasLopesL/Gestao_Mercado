# Usar uma imagem base do Python
FROM python:3.11

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar os arquivos de requisitos para o contêiner
COPY requirements.txt /app/

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação para o contêiner
COPY . .

# Expôr a porta que o Flask usará
EXPOSE 5000

# Definir o comando para rodar o Flask
CMD ["python", "run.py"]