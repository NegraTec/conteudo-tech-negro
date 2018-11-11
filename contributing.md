# Contribuindo

# O que instalar antes

- Docker

## Executando o projeto

1. Clone o projeto para sua máquina

2. Dentro da pasta do projeto execute `docker build -t conteudo-tech-negro .`

3. Adicione um arquivo chamado .env com as variaveis sugeridas no `.env-sample`.

4. Para iniciar o servidor execute `docker-compose up`

5. Acesse `http://localhost:5000`

## Migração do banco de dados

Após mudanças nas tabelas, executar os comandos `docker-compose exec web flask db migrate` e depois `docker-compose exec web flask db upgrade`

Para mais informações, acesse a documentação do [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

Documentação do [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

**O banco possui backup agendados para as 23 hs todos os dias.**

## Deploy

Usamos Heroku.
https://conteudo-tech-negro.herokuapp.com

**Variáveis de ambiente**

`URL_BANCO_DADOS`

Novas variáveis de ambiente devem ser adicionadas no arquivo `.env-sample`

