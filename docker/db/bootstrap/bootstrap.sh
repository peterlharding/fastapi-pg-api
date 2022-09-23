#!/bin/sh

echo "Bootstrapping users..."

sleep 2
su - postgres -c "psql  < /tmp/init_db.sql"
echo "Init exit status |$?|"

echo "Completed init"

sleep 1
su - postgres -c "psql fastapi < /tmp/backup.sql"
echo "DB load exit status |$?|"

