# Imagem do Python
FROM python:3.11

# Diretório no conteiner
WORKDIR /app

# Copia as dependências
COPY requirements.txt /app/

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do código para o contêiner
COPY . .

# Porta do Flask
EXPOSE 5000

# Comando para rodar o Flask
CMD ["python", "run.py"]