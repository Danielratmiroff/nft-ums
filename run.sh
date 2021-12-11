#!/bin/bash
cd /home/ec2-user/ums
docker-compose rm &&
    docker-compose build --no-cache &&
    # docker-compose --env-file ~/.env up -d --force-recreate
    docker-compose -d --force-recreate
