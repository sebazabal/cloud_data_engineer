#!/usr/bin/env bash


set -e

echo "docker stop all running containers"
docker stop $(docker ps -a -q)

echo "docker rm all containers"
docker rm $(docker ps -a -q)

echo "docker remove all images"
docker rmi $(docker images -q)


echo "docker compose down, removing network"
docker-compose down -v

echo "docker compose up --build"
docker-compose up --build


