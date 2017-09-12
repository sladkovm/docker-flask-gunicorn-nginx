FROM python:3.6.2

RUN mkdir -p /home/project/flask_app
WORKDIR /home/project/flask_app
COPY requirements.txt /home/project/flask_app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/flask_app

