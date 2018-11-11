# Contribuindo

# O que instalar antes

- Docker

## Executando o projeto

1. Clone o projeto para sua máquina

2. Dentro da pasta do projeto execute `docker build -t conteudo-tech-negro .`

3. Para iniciar o servidor execute `docker run --rm -it -v "$PWD":/usr/src/app -w /usr/src/app -p 5000:5000 --env-file .env conteudo-tech-negro`

4. Acesse `http://localhost:5000`