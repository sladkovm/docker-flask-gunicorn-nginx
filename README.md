# Blueprint for docker-flask-gunicorn-nginx web application

![Example App](app_example.jpg?raw=true "Example App")

Bootstrap example of a *Flask/Dash* app served via *Gunicorn* and *Nginx* using Docker containers

Guildeline article can be found at https://sladkovm.github.io/webdev/2017/10/16/Deploying-Plotly-Dash-in-a-Docker-Container-on-Digitital-Ocean.html

## Run

```bash
make build
```

In your browser (assuming the docker-machine runs on 192.168.99.100) go to:

    http://192.168.99.100

To clean up the container mess, run
```
make clean
```

It will shut down all container and remove all images

## Prominent features:

1. Dockerized application orchestrated by docker-compose
2. Gunicorn as a WSGI and Nginx as a reverse proxy are included as services
3. Nginx is configured to serve static files, e.g. images, css etc.
4. Example of routing implementation in *Dash* app is shown
5. Build process uses *requirements.txt*, but *Pipenv* files are included to ease the development process
6. Bootstrap css is included
7. Standard Single Page App Layout with Header, Main and Footer is set up
