<img width="1000" alt="logo" src="https://github.com/user-attachments/assets/f8bde5ae-8a5d-4da0-9bdf-5d8b18c939ab" />

# 🗓️ DAYPACE

Ferramenta de gestão de projetos e rotinas com quadro Kanban

**Tecnologias usadas:** Docker, HTML, CSS, JavaScript, Django, Django REST, SQLite, Python.
## 📹  Exemplo

https://github.com/user-attachments/assets/658b4603-ca0f-447b-8f9d-764422a7c19b

## ▶️ Rodar

### 🐍 Python 3.12
#### Baixar dependências
`pip install --no-cache-dir -r asgiref
Django
django-cors-headers
djangorestframework
sqlparse`
#### Rodar o servidor 

```
python backend/manage.py makemigrations
python backend/manage.py migrate
python backend/manage.py runserver
```

### 🐳 Docker
#### Criar imagem:
`docker build -t daypace https://github.com/Gabriel-H-P-Leite/Daypace.git#main`
#### Rodar o container:
`docker run -d --name Daypace -p 8000:8000 daypace`
