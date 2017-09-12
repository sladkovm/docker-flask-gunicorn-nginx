# docker-flask-gunicorn-nginx
Bootstrap example of a Flask app served via Gunicorn and Nginx using Docker conteiners


### Run

/bin/bash run_docker.sh

1. It will delete all running containers and kill all running docker process.
2. Will start all required containers in background

### In your browser (assuming you run it on a local machine)

http://localhost - the app

http://localhost/api - the API endpoint

http://localhost/api/resource - the API resource
