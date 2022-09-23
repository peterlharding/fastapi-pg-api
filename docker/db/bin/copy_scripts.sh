#!/bin/sh

set -x

ID=`docker container ps | grep fastapi-db | awk '{print $1}'`

echo "Copying scripts to $ID"

docker cp bootstrap/bootstrap.sh      $ID:/tmp
docker cp bootstrap/init_db.sql       $ID:/tmp
docker cp bootstrap/grant.sql         $ID:/tmp
docker cp bootstrap/backup.sql        $ID:/tmp/backup.sql

