# docker-flask-gunicorn-nginx
Bootstrap example of a Flask/Dash app served via Gunicorn and Nginx using Docker containers

Guildeline article can be found at https://sladkovm.github.io/webdev/2017/10/16/Deploying-Plotly-Dash-in-a-Docker-Container-on-Digitital-Ocean.html

### Run

/bin/bash run_docker.sh

1. It will kill all running docker processes.
2. Will start all required containers in background

### In your browser (assuming the docker-machine runs on 192.168.99.100)

http://192.168.99.100
