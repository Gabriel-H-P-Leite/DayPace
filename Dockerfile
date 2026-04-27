#base
FROM python:3.12
#evita cache
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
#diretorio no container
WORKDIR /app
#dependencias
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#copia o projeto
COPY . .
#porta
EXPOSE 8000
CMD ["./app/init"]
