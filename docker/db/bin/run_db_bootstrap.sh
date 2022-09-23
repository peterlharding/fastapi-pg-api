#!/bin/sh

ID=`docker container ps | grep fastapi-db | awk '{ print $1}'`

echo "ContainerId - ${ID}"

docker exec  -it ${ID} /tmp/bootstrap.sh

