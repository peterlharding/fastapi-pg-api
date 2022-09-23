
# -----------------------------------------------------------------------------

NET      = fastapi-api-db-net
PG_DATA  = fastapi-api-pg-data

# -----------------------------------------------------------------------------

add-net:
	docker network create $(NET)

ls-net:
	docker network list

rm-net:
	docker network remove $NET)

# -----------------------------------------------------------------------------

ls-vols:
	docker volume list

add-vol:
	docker volume create $(PG_DATA)

# -----------------------------------------------------------------------------

ls:	ls-vols ls-net

# -----------------------------------------------------------------------------

up:
	docker compose up -d
	docker container ps
	-netstat -an | egrep "5432|8088"


down:
	docker compose down
	docker container ps
	-netstat -an | egrep "5432|8088"

# -----------------------------------------------------------------------------

reset:
	./bin/reset.sh

setup:
	./bin/setup.sh

# -----------------------------------------------------------------------------

