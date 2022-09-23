#!/usr/bin/env python3

import sys

from datetime import datetime

from dateutil import parser as datetime_parser
from dateutil.tz import tzutc

from hashlib import md5

from sqlalchemy import create_engine, MetaData, Table, text, func, desc, asc, extract

from sqlalchemy import (
    Column,
    Boolean,
    Date,
    DateTime,
    Integer,
    String,
    Text,
    Time,
    text
)

from sqlalchemy.dialects.mysql import (
    CHAR
)

from sqlalchemy.ext.hybrid import (
    hybrid_property,
    hybrid_method
)

# ------------------------------------------------------------------------------

from .. import app, Base


# ==============================================================================
# This models file defines:
#
#    UserDetails
#
# ==============================================================================
"""
auth=# \d application_user;
                                          Table "public.user_details"
    Column     |            Type             | Collation | Nullable |                 Default
---------------+-----------------------------+-----------+----------+------------------------------------------
 id            | integer                     |           | not null | nextval('user_details_id_seq'::regclass)
 user_id       | character varying(64)       |           | not null |
 username      | character varying(64)       |           | not null |
 password      | character varying(128)      |           | not null |
 email         | character varying(128)      |           | not null |
 first_name    | character varying(64)       |           | not null |
 last_name     | character varying(64)       |           | not null |
 notes         | text                        |           |          | ''::text
 is_admin      | boolean                     |           |          | true
 is_active     | boolean                     |           |          | true
 last_login    | timestamp without time zone |           | not null |
 when_created  | timestamp without time zone |           | not null |
 when_modified | timestamp without time zone |           | not null |
Indexes:
    "user_details_pkey" PRIMARY KEY, btree (id)
    "user_details_user_id_key" UNIQUE CONSTRAINT, btree (user_id)
    "user_details_username_key" UNIQUE CONSTRAINT, btree (username)

"""
# ------------------------------------------------------------------------------

class ApplicationUser(Base):

    __tablename__  = 'application_user'

    id             = Column(Integer, primary_key=True)
    user_id        = Column(String(64), unique=True, nullable=False)
    username       = Column(String(64), unique=True, nullable=False)
    password       = Column(String(128), nullable=False)
    email          = Column(String(128), nullable=False)
    first_name     = Column(String(64), unique=True, nullable=False)
    last_name      = Column(String(64), unique=True, nullable=False)
    notes          = Column(Text)
    is_admin       = Column(Boolean)
    is_active      = Column(Boolean)
    last_login     = Column(DateTime, nullable=False)
    when_created   = Column(DateTime, nullable=False)
    when_modified  = Column(DateTime, nullable=False)

    # -------------------------------------------------------------------------

    def __init__(self, username):
        self.username        = username
        self.created_on      = datetime.now()

    # -------------------------------------------------------------------------

    def __repr__(self):
        return '<id: username: {}'.format(self.username)

    # -------------------------------------------------------------------------

    def jsonify(self):
         return {
                    'id': self.id,
                    'userId': self.user_id,
                    'username': self.username,
                    'password': self.password,
                    'email': self.email,
                    'firstName': self.first_name,
                    'lastName': self.last_name,
                    'notes': self.notes,
                    'isAdmin': self.is_admin,
                    'isActive': self.is_active,
                    'lastLogin': self.last_login.strftime('%Y-%m-%d %H:%M:%S'),
                    'whenCreated': self.when_created.strftime('%Y-%m-%d %H:%M:%S'),
                    'whenModified': self.when_modified.strftime('%Y-%m-%d %H:%M:%S')
                }


    # ---------------------------------------------------------------------

    @hybrid_method
    def is_correct_password(self, password):
        return self.password == password

    # -------------------------------------------------------------------------

# ==============================================================================
