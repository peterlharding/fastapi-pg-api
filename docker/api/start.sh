#!/bin/sh

PORT=`grep PORT .env | sed 's/PORT=//'`
HOST='0.0.0.0'

echo $PORT

uvicorn app.main:app --reload --host ${HOST} --port ${PORT}

