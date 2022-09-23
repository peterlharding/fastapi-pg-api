
# Overview

An overview of the setup tasks

## The backup image

Get the backup image to use in the docker container

```
apt-get update

apt install -y vim net-tools procps openssh-client

mkdir /u
mkdir /u/db

cd /u/db

scp xxxx:backup.sql .
```

## Setup postgres

```
su - postgres

createuser root
createuser api

createdb root
createdb fastapi
createdb api
```

-- OR in psql

```
create database root
create database fastapi
create database api
```

## Set password for api user.

```
ALTER USER 'api' SET PASSWORD 'Secret'

```






