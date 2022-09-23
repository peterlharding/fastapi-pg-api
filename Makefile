

FILES := $(shell ls)
PORT  := $(shell grep PORT .env | sed 's/PORT=//')

start:
	uvicorn app.main:app --reload --port $(PORT)

chown:
	chown -R www-data:www-data .

install:
	python3 -m pip install -r requirements.txt

setup:
	-ln env.template app/.env

ls:
	echo "FILES |$(FILES)|"
	echo "PORT |$(PORT)|"

