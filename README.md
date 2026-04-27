<img width="1000" alt="logo" src="https://github.com/user-attachments/assets/f8bde5ae-8a5d-4da0-9bdf-5d8b18c939ab" />

# DAYPACE

Ferramenta de gestão de projetos e rotinas com quadro Kanban

**Tecnologias usadas:** Docker, HTML, CSS, JavaScript, Django, Django REST, SQLite, Python.

## Rodar
### Python 3.12
#### Dependencias
`asgiref==3.11.1
Django==6.0.2
django-cors-headers==4.9.0
djangorestframework==3.16.1
sqlparse==0.5.5`
### Docker
#### Criar imagem:
`docker build -t daypace https://github.com/Gabriel-H-P-Leite/Daypace.git#main`
#### Rodar o container:
`docker run -d --name Daypace -p 8000:8000 daypace`
