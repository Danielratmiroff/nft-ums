#!/bin/bash
cd /home/ec2-user/ums
docker-compose build --no-cache
MONGO_USER=$MONGO_USER MONGO_PASSWORD=$MONGO_PASSWORD MONGO_IP=$MONGO_IP MONGO_PORT=$MONGO_PORT docker-compose up -d