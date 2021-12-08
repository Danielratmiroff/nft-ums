#!/bin/bash
cd /home/ec2-user/ums
docker-compose build --no-cache
docker-compose up -d