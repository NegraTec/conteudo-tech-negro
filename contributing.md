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

Após mudanças nas tabelas, executar os comandos `docker-compose exec web flask db migrate` e depois `docker-compose exec web flask db upgrade` (com o servidor executando).

Para mais informações, acesse a documentação do [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/)

Alembic https://alembic.zzzcomputing.com/en/latest/tutorial.html#create-a-migration-script

Documentação do [Flask SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/)

**O banco possui backup agendados para as 23 hs todos os dias.**

## Testes

`docker run --rm -it -v "$PWD":/usr/src/app -w /usr/src/app conteudo-tech-negro_web pytest -W ignore::DeprecationWarning`

## Deploy

Usamos Heroku.
https://conteudo-tech-negro.herokuapp.com

**Variáveis de ambiente**

`URL_BANCO_DADOS`

Novas variáveis de ambiente devem ser adicionadas no arquivo `.env-sample`

Com **GCP**, o arquivo `env.yaml` é encriptado usando [Google KMS](https://cloud.google.com/kms/).

É possível usar o CLI gcloud com a [imagem Docker google/cloud-sdk](https://hub.docker.com/r/google/cloud-sdk).

Peça para ser adicionada no projeto GCP e coloque suas credenciais no gcloud usando `docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud auth login`. Depois configure o projeto com `docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud config set project <GCP-project>`

Peça o GCP-project a outra colaboradora do repositório.

Para encriptar o arquivo: `docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud kms encrypt --location global \
  --keyring storage --key mykey \
  --plaintext-file env.yaml \
  --ciphertext-file env.yaml.encrypted`
  
Para desencriptar o arquivo: `docker run -v "$PWD":/root/.config -w /root/.config -ti google/cloud-sdk:latest gcloud kms decrypt --location global \
  --keyring storage --key mykey \
  --plaintext-file env.yaml \
  --ciphertext-file env.yaml.encrypted`

