FROM python:3.6.2

RUN mkdir -p /home/project/flask_api
WORKDIR /home/project/flask_api
COPY requirements.txt /home/project/flask_api
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/flask_api

