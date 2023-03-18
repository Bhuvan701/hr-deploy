FROM python:3.12.0a6-slim-buster

WORKDIR /app

COPY ./resume ./

RUN pip install --upgrade pip --no-cache-dir

RUN apt-get update -y

RUN apt-get install -y python-reportlab

RUN pip install -r /app/requirements.txt --no-cache-dir

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 





CMD ["gunicorn","resume.wsgi:application","--bind","0.0.0.0:8000"]
