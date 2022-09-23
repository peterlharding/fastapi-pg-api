#!/bin/sh
#
# You need to run reset.sh to kill the old data volume
#
# -----------------------------------------------------------------------------

VOLUME=fastapi-api-pg-data

docker container ps

RC=`docker container ps | grep fastapi-db | wc -l`

if [ ${RC} -eq 1 ] ; then
    echo "Shutdown the environment before resetting the database!"
    docker container ps
    exit 1
fi

# Now check that the volume has been created

RC=`docker volume list | grep $VOLUME | wc -l`

if [ ${RC} -eq 1 ] ; then
    echo "Data volume ${VOLUME} is there OK"
fi

# Now bring up the DB backend

echo "Bringing up the backend"

docker compose up -d

sleep 2

docker container ps

./bin/copy_scripts.sh
./bin/run_db_bootstrap.sh

