<img width="3508" height="715" alt="logo" src="https://github.com/user-attachments/assets/f8bde5ae-8a5d-4da0-9bdf-5d8b18c939ab" />

Criar imagem:
`docker build -t daypace https://github.com/Gabriel-H-P-Leite/Daypace.git#main`

Rodar o container:
`docker run -d \
  --name Daypace \
  -p 8000:8000 \
  daypace`

