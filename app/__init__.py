#!/usr/bin/env python3
#
# -----------------------------------------------------------------------------
"""
  Setup module for FastAPI application

"""
# -----------------------------------------------------------------------------

import os
import uuid
import bcrypt
import logging

from fastapi import FastAPI

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# -----------------------------------------------------------------------------

from .CONFIG import (
    URI_TEMPLATE,
    DBHost,
    DBName,
    DBUser,
    LogName,
    Title,
    Version
)

from .PASSWORD import DBPassword

SQLALCHEMY_DATABASE_URI = URI_TEMPLATE % (DBUser, DBPassword, DBHost, DBName)



# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------

UUID      = os.getenv('UUID', default=uuid.uuid4())
HOST      = os.getenv('HOST', default='127.0.0.1')

# -----------------------------------------------------------------------------

logger    = logging.getLogger("hsdb")

print(f"Using LogName |{LogName}|")

logging.basicConfig(filename=LogName,
                    filemode='a',
                    format='%(asctime)s  %(levelname)-8s  %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

# -----------------------------------------------------------------------------
# Set up tha application
# -----------------------------------------------------------------------------

app             = FastAPI(title=Title, version=Version)

app.logger      = logger
app.__version__ = Version

# -----------------------------------------------------------------------------
# Setup the DB connection
# -----------------------------------------------------------------------------

engine       = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base         = declarative_base()

# -----------------------------------------------------------------------------
# Dependency
# -----------------------------------------------------------------------------

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# -----------------------------------------------------------------------------


