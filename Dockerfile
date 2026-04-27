FROM python:3.12

RUN apt-get update && apt-get install -y git

WORKDIR /app

# clona o repositório
RUN git clone https://github.com/seu-usuario/seu-repo.git .

# instala dependências
RUN pip install --no-cache-dir -r backend/requirements.txt

EXPOSE 8000

CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]