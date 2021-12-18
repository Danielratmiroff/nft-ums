#!/bin/bash
cd /home/ec2-user/ums
docker-compose rm -f &&
    docker-compose build --no-cache &&
    docker-compose up -d --force-recreate
