#!/bin/bash
cd /home/ec2-user/ums
docker-compose rm --all &&
docker-compose build --no-cache &&
docker-compose --env-file ~/.env up up -d --force-recreate