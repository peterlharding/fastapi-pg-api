# encoding: utf-8
#
# DB Version: 0.8.25
#       Date: 2020-11-03
#
# -----------------------------------------------------------------------------

import sys

from datetime import datetime, timedelta

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    Integer,
    String,
    Text,
    Time,
    text
)

from sqlalchemy.dialects.postgresql import (
    BOOLEAN,
    TIMESTAMP
)

from sqlalchemy.ext.hybrid import (
    hybrid_property,
    hybrid_method
)

# -----------------------------------------------------------------------------

from .. import app, Base

#==============================================================================
"""
# \d db_metadata
                                        Table "public.db_metadata"
   Column        |            Type             | Collation | Nullable |                 Default
-----------------+-----------------------------+-----------+----------+-----------------------------------------
 id              | integer                     |           | not null | nextval('db_metadata_id_seq'::regclass)
 release         | character varying(64)       |           | not null |
 db_version      | character varying(64)       |           | not null |
 notes           | text                        |           | not null |
 when_modified   | timestamp without time zone |           |          | CURRENT_TIMESTAMP
Indexes:
    "db_metadata_pkey" PRIMARY KEY, btree (id)

"""
# -----------------------------------------------------------------------------

class DbMetadata(Base):

    __tablename__ = 'db_metadata'

    id            = Column(Integer, primary_key=True)
    release       = Column(String(64))
    db_version    = Column(String(64))
    notes         = Column(Text)
    when_modified = Column(DateTime)

    #----------------------------------------------------------------------

    def __str__(self):
         return "<DbMetadata: %r': '%s'>" % (self.id, self.db_version)

    #----------------------------------------------------------------------

    def __repr__(self):
         return "('%s', '%s')" % (self.id, self.db_version)

    #----------------------------------------------------------------------

    def jsonify(self):

         return {
                    'id'            : self.id,
                    'release'       : self.release,
                    'dbVersion'     : self.db_version,
                    'notes'         : self.notes,
                    'whenModified'  : self.when_modified.strftime('%Y-%m-%d %H:%M:%s')
                }

    #----------------------------------------------------------------------

# ============================================================================
