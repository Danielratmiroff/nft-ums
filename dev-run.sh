#!/bin/bash
docker-compose rm &&
    docker-compose build --no-cache &&
    docker-compose --env-file ./.env up --force-recreate
