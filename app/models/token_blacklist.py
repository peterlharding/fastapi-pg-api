#!/usr/bin/env python3

import sys

from datetime import datetime

from dateutil import parser as datetime_parser
from dateutil.tz import tzutc

from hashlib import md5

from sqlalchemy import create_engine, MetaData, Table, text, func, desc, asc, extract

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

from sqlalchemy.dialects.mysql import (
    CHAR
)

from sqlalchemy.ext.hybrid import (
    hybrid_property,
    hybrid_method
)

# ------------------------------------------------------------------------------

from .. import app, Base, SessionLocal

# ==============================================================================

class TokenBlacklist(Base):

    __tablename__ = 'token_blacklist'

    id             = Column(Integer, primary_key=True)
    token          = Column(String(512), unique=True, nullable=False)
    expiry         = Column(DateTime, nullable=False)
    blacklisted_on = Column(DateTime, nullable=False)

    #---------------------------------------------------------------------------

    def __init__(self, token):
        self.token          = token
        self.blacklisted_on = datetime.now()

    #---------------------------------------------------------------------------

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    #---------------------------------------------------------------------------

    @classmethod
    def test(cls):

        return True

    #---------------------------------------------------------------------------

    @classmethod
    def check_blacklist(cls, auth_token):

        # check whether auth token has been blacklisted

        # app.logger.info("[TokenBlacklist::check_blacklist]       auth_token |%s|" % auth_token)

        db = SessionLocal()

        res = db.query(TokenBlacklist).filter_by(token=str(auth_token)).first()

        if res:
            return True
        else:
            return False

    #---------------------------------------------------------------------------


# ==============================================================================

