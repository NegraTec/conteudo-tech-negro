FROM python:3.7.1-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

# evita o problema de não encontrar o pg_config para a biblioteca psycopg2
RUN apk update && \
 apk add postgresql-libs && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . .

EXPOSE 8080

CMD gunicorn --log-level DEBUG --bind=0.0.0.0:8080 app:app
