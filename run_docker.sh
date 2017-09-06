#!/usr/bin/env bash

echo killing old docker processes
docker-compose rm -f

echo building docker containers
docker-compose build

echo runnung docker containers
docker-compose up -d

echo the app is served at 127.0.0.1 on the locahost or at the IP address git sttof the server