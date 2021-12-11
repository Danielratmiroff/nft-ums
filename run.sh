#!/bin/bash
cd /home/ec2-user/ums
docker-compose down && docker-compose rm &&
    docker-compose build --no-cache &&
    docker-compose up --env-file ~/.env -d --force-recreate
