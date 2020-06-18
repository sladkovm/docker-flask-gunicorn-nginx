FROM python:3.7.7-slim-buster

RUN mkdir -p /home/project/dash_app
WORKDIR /home/project/dash_app
COPY requirements.txt /home/project/dash_app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/dash_app

