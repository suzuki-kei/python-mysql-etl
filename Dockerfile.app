FROM python:3

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
COPY ./src /app/src
COPY ./config /app/config

RUN pip install -r requirements.txt

