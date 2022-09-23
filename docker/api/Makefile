
IMGNAME = 'fastapi-pg-api'

# ----- Environment Setup -----------------------------------------------------

setup:
	docker compose down
	cp ../../requirements.txt .
	cp ../../.env .
	-rm -rf app
	cp -r ../../app .
	cp CONFIG.py app
	-docker image rm $(IMGNAME)

# ----- Docker Commands -------------------------------------------------------

build:
	docker build -t $(IMGNAME) .

run:
	docker run -it --rm -d --name $(IMGNAME)  $(IMGNAME)
	docker ps -a

logs:
	docker logs $(IMGNAME)

stop:
	d-stop $(IMGNAME)

sh:
	docker exec -it $(IMGNAME) bash

ls-net:
	docker network list

ls-vol:
	docker volume list

ls:	ls-net ls-vol

# ----- Docker Compose commands -----------------------------------------------

local-drun:
	# docker run $(IMGNAME) --publish 127.0.0.1:8000:8000 --name $(IMGNAME) & 
	docker run -itd --rm --name $(IMGNAME) --publish 127.0.0.1:8000:8000 $(IMGNAME)
	sleep 1
	docker ps -a

# ----- Docker Compose commands -----------------------------------------------

up:
	docker compose up -d
	docker ps

down:
	docker compose down
	docker ps

# -----------------------------------------------------------------------------
# For adminer access:
# Browse to - http://localhost:8088/?pgsql=fastapi-db&username=root&db=secret&ns=public

