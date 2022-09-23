#!/bin/sh

echo
echo
echo "Pulling down existing PostgreSQL data volume for re-initialization"
echo

RC=`docker container ps | grep fastapi-db | wc -l`

echo "RC |${RC}|"

if [ ${RC} -eq 1 ] ; then
    echo "Shutdown the environment before resetting the database!"
    docker compose down
    sleep 2
    docker container ps
fi

VOLUME=fastapi-api-pg-data

RC=`docker volume list | grep $VOLUME | wc -l`

if [ ${RC} -eq 1 ] ; then
    echo "Deleting volume - ${VOLUME}"
    docker volume rm ${VOLUME}
    docker volume list
fi

echo "Recreating volume - ${VOLUME}"

docker volume create ${VOLUME}

docker volume list

docker container ps

