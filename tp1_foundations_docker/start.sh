#!/usr/bin/env bash


set -e
docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

docker rmi $(docker images -q)

docker-compose down -v

docker-compose up --build

#echo "ejecuta wait-until"
#source .env
#./wait-until "docker-compose exec -T -e PGPASSWORD=${POSTGRES_PASSWORD} db_postgres psql -U ${POSTGRES_USER} ${POSTGRES_DB} -c 'select 1'"
#./wait-until "pg_isready -U postgres"

#echo "termina el wait-until"

#./wait-until "docker-compose exec pycont /app/add_data.py"
#exec "$@"
#docker-compose exec pycont python 
#echo "pycont"
