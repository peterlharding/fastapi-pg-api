#!/usr/bin/env python3

from fastapi import app as application

HOST = "0.0.0.0"
PORT = 4000

if __name__ == "__main__":

        uvicorn app.main:app --reload --port $(PORT)


