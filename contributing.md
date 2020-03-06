# Contribuindo

# O que instalar antes

- Docker
- [Docker Compose](https://docs.docker.com/compose/install/), se você nâo instalar pelo Docker for Windows/Mac ou Docker Toolbox

## Arquitetura

![diagrama-de-contexto](/arquitetura/diagrama-contexto.png)

![diagrama-de-container](/arquitetura/diagrama-container.png)

![diagrama-de-componente](/arquitetura/diagrama-componente.png)

![diagrama-de-classe](/arquitetura/diagrama-classe.png)

Usamos o GraphViz para gerar os diagramas. Os diagramas ficam na pasta `arquitetura`.

Comando para criar novo diagrama a partir de um arquivo .dot: `docker run -it --rm -v $(pwd):/data risaacson/graphviz:latest dot -v -Tpng /data/arquitetura/<nome-arquivo>.dot -o /data/arquitetura/<nome-arquivo>.png`

## Executando o projeto

1. Clone o projeto para sua máquina

2. Adicione um arquivo chamado `.env` com as variaveis sugeridas no `.env-sample`.

3. Para iniciar o servidor execute `sh cli/conteudo.sh roda-projeto`

4. Acesse `http://localhost:5000`

Uma boa fonte de consulta de como o projeto é desenvolvido: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Migração do banco de dados

Após mudanças nas tabelas, executar os comandos `docker-compose exec web flask db migrate` e depois reinicie o servidor. **O comando de upgrade do banco é executado ao iniciar o servidor Flask (olhe em app/__init__.py).**

Para mais informações, acesse a documentação do [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

Alembic https://alembic.zzzcomputing.com/en/latest/tutorial.html#create-a-migration-script

Documentação do [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)


## Testes

`sh cli/conteudo.sh testes`

## CI/CD

O projeto usa o [Travis CI](https://travis-ci.org/).

Para o deploy temos o arquivo com as credenciais do GCP encriptado. Para encriptar usamos o travis cli através de um container docker.

[Criando as credenciais](https://docs.travis-ci.com/user/deployment/google-app-engine/)

Comando para encriptar o arquivo de credenciais:

1. Construa a imagem para o travis cli com `sh ci/compras.sh build-travis-cli` 

2. Entre no container travis-cli com o comando `sudo docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp travis-cli /bin/bash`
3. Então execute `travis encrypt-file conteudo-negro-tech-c463a08bcb68.json --add`

## Deploy

**Variáveis de ambiente**

`URL_BANCO_DADOS`

Novas variáveis de ambiente devem ser adicionadas no arquivo `.env-sample`

Usamos Heroku.
https://conteudo-tech-negro.herokuapp.com

