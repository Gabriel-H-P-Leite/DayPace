<img width="1000" alt="logo" src="https://raw.githubusercontent.com/Gabriel-H-P-Leite/DayPace/refs/heads/main/frontend/img/logo.png" />

# 🗓️ DAYPACE

Ferramenta de gestão de projetos e rotinas com quadro Kanban

**Tecnologias usadas:** Docker, HTML, CSS, JavaScript, Django, Django REST, SQLite, Python.
## 📹  Exemplo

[exemplo.webm](https://github.com/user-attachments/assets/e26abedc-518f-40fd-b289-69e2a04dbca3)


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
