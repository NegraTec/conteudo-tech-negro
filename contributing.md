# Contribuindo

# O que instalar antes

- Docker

## Executando o projeto

1. Clone o projeto para sua máquina

2. Adicione um arquivo chamado .env com as variaveis sugeridas no `.env-sample`.

3. Para iniciar o servidor execute `docker-compose up --build`

4. Acesse `http://localhost:5000`

Uma boa fonte de consulta de como o projeto é desenvolvido: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

## Migração do banco de dados

Após mudanças nas tabelas, executar os comandos `docker-compose exec web flask db migrate` e depois reinicie o servidor. **O comando de upgrade do banco é executado ao iniciar o servidor Flask (olhe em app/__init__.py).**

Para mais informações, acesse a documentação do [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

Alembic https://alembic.zzzcomputing.com/en/latest/tutorial.html#create-a-migration-script

Documentação do [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

**O banco possui backup agendados para as 8PM-12AM todos os dias.**

## Testes

**É necessário configurar a variável de ambiente `TESTES` para True para que os testes unitários tentem configurar o banco.** 

`docker run --rm -it -v "$PWD":/usr/src/app -w /usr/src/app -e TESTES=True conteudo-tech-negro_web pytest -W ignore::DeprecationWarning`

## Deploy

**Variáveis de ambiente**

`URL_BANCO_DADOS`

Novas variáveis de ambiente devem ser adicionadas no arquivo `.env-sample`

Temos o ambiente implantado no GCP: http://conteudo-negro-tech.appspot.com/

*Configurar o Google Cloud localmente*

Peça para ser adicionada no projeto GCP e coloque suas credenciais e configure o projeto google na sua máquina com `sh cli/conteudo.sh configura-projeto-google`

Peça o GCP-project a outra colaboradora do repositório.

*Encriptação de arquivos de ambiente*

Com **GCP**, o arquivo `env.yaml` é encriptado usando [Google KMS](https://cloud.google.com/kms/).

Para encriptar o arquivo: `sh cli/conteudo.sh encripta-env-yaml`
  
Para desencriptar o arquivo: `sh cli/conteudo.sh desencripta-env-yaml`

É possível usar o CLI gcloud com a [imagem Docker google/cloud-sdk](https://hub.docker.com/r/google/cloud-sdk).

## Débito Técnico

Usamos Heroku.
https://conteudo-tech-negro.herokuapp.com

