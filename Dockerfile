#imagem python
FROM python:3.12
#diretorio principal
WORKDIR /app
#instala dependencias
RUN pip install --no-cache-dir -r backend/requirements.txt
EXPOSE 8000
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8000"]
