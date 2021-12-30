#!/bin/bash
if [ "$1" = "-d" ]; then
    docker-compose rm -f &&
        docker-compose build --no-cache &&
        docker-compose up -d --force-recreate
else
    docker-compose rm -f &&
        docker-compose build --no-cache &&
        docker-compose up --force-recreate
fi
