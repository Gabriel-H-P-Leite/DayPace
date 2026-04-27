# imagem base
FROM python:3.12

# evita cache de bytecode
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# diretório dentro do container
WORKDIR /app

# copia dependências
COPY backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copia o projeto
COPY . .

# porta do Django
EXPOSE 8000

# comando pra rodar
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]
