# encoding: utf-8

import sys

from datetime import datetime

from dateutil import parser as datetime_parser
from dateutil.tz import tzutc

from hashlib import md5

from sqlalchemy import (
    Column,
    Integer,
    String,
)

from sqlalchemy.dialects.mysql import (
    CHAR
)


# -----------------------------------------------------------------------------

from .. import app, Base


# ==============================================================================
"""
api=> \d+ iso_country
                                       Table "public.iso_country"
 Column |         Type          | Collation | Nullable | Default | Storage  | Stats target | Description
--------+-----------------------+-----------+----------+---------+----------+--------------+-------------
 code   | character varying(2)  |           | not null |         | extended |              |
 iso3   | character varying(3)  |           | not null |         | extended |              |
 num3   | integer               |           | not null |         | plain    |              |
 name   | character varying(64) |           | not null |         | extended |              |
Indexes:
    "iso_country_pkey" PRIMARY KEY, btree (code)

"""
# -----------------------------------------------------------------------------

class ISO_Country(Base):

    __tablename__ = 'iso_country'

    code          = Column(CHAR(2), primary_key=True)
    iso3          = Column(CHAR(3))
    num3          = Column(Integer)
    name          = Column(String(64))

    # ---------------------------------------------------------------------

    def __str__(self):
         return "'%s': '%s'" % (self.code, self.name)

    # ---------------------------------------------------------------------

    def __repr__(self):
         return "'%s': '%s'" % (self.code, self.name)

    # ---------------------------------------------------------------------

    def jsonify(self):
         return {
                    'code': self.code,
                    'iso3': self.iso3,
                    'num3': self.num3,
                    'name': self.name.rstrip()
                }

    # ---------------------------------------------------------------------

# =============================================================================

