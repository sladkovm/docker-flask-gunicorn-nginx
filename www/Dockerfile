FROM python:3.6.2

RUN mkdir -p /home/project/www
WORKDIR /home/project/www
COPY requirements.txt /home/project/www
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/project/www

EXPOSE  8000
CMD gunicorn -w 2 --bind 0.0.0.0:8000 app:server