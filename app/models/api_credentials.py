#!/usr/bin/env python3

import sys
import bcrypt

from datetime import datetime

from dateutil import parser as datetime_parser
from dateutil.tz import tzutc

from hashlib import md5

from sqlalchemy import (
    Column,
    Integer,
    String,
)

from sqlalchemy.ext.hybrid import (
    hybrid_property,
    hybrid_method
)


#-------------------------------------------------------------------------------

from .. import app, Base

# ==============================================================================
"""
auth=# \d api_credentials;
                                        Table "public.api_credentials"
     Column      |          Type          | Collation | Nullable |                 Default
-----------------+------------------------+-----------+----------+-----------------------------------------
 id              | integer                |           | not null | nextval('credentials_id_seq'::regclass)
 user_id         | character varying(64)  |           |          |
 email           | character varying(64)  |           | not null |
 hashed_password | character varying(128) |           | not null |
Indexes:
    "credentials_pkey" PRIMARY KEY, btree (id)
    "credentials_email_key" UNIQUE CONSTRAINT, btree (email)
    "credentials_user_id_key" UNIQUE CONSTRAINT, btree (user_id)

"""
#-------------------------------------------------------------------------------

class ApiCredentials(Base):

    __tablename__ = 'api_credentials'

    id              = Column(Integer, primary_key=True)
    user_id         = Column(String(64))
    email           = Column(String(64))
    hashed_password = Column(String(128))

    #----------------------------------------------------------------------

    def __init__(self, email, password):
        self.email = email
        self.password = password
        # self.authenticated = False

    #----------------------------------------------------------------------

    def __str__(self):
         return "'%s': '%s'" % (self.email, self.hashed_password)

    #----------------------------------------------------------------------

    def __repr__(self):
         return "'%s': '%s'" % (self.email, self.hashed_password)

    #----------------------------------------------------------------------

    @hybrid_property
    def password(self):
        return self.hashed_password

    #----------------------------------------------------------------------

    @password.setter
    def set_password(self, plaintext_password):
        pass

    #----------------------------------------------------------------------

    @hybrid_method
    def is_correct_password(self, hashed_password):
        return self.hashed_password == hashed_password

    #----------------------------------------------------------------------

    def is_correct_password_hash(self, plaintext_password):
        pass

    #----------------------------------------------------------------------

    def jsonify(self):
        return {
                   'id': self.id,
                   'userId': self.user_id,
                   'email': self.email,
                   'hashedPassword;': self.hashed_password,
               }

    #----------------------------------------------------------------------

    def verify_password(self, password):
        pass 
        # return self.password_hash ==  bcrypt.generate_password_hash(password).decode('utf-8')

    #---------------------------------------------------------------------------

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['Guid'])

    #---------------------------------------------------------------------------

    @classmethod
    def SetFromForm(cls, this, form):

        this.hashed_password  = form['HashedPassword']

    #---------------------------------------------------------------------------

    @classmethod
    def Save(cls, form):

        email = int(form['email'])

        this = ApiCredentials.query.filter_by(email=email).first()

        ApiCredentials.SetFromForm(this, form)

        session.flush()
        session.commit()

    #---------------------------------------------------------------------------

    @classmethod
    def Add(cls, form, db):

        this = ApiCredentials()

        ApiCredentials.SetFromForm(this, form)

        sql = text("SELECT MAX(id) from ApiCredentials")

        next_id = db.execute(sql).first()[0] + 1

        app.logger.info('[ApiCredentials::Add]                      next_id |%d|' % next_id)

        this.Id = next_id

        session.add(this)

        session.flush()
        session.commit()

    #---------------------------------------------------------------------------

    @classmethod
    def Save(cls, form):

        email = int(form['email'])

        app.logger.info('[ApiCredentials::Save]                       email |%d|' % email)

        this = ApiCredentials.query.filter_by(email=email).first()

        ApiCredentials.SetFromForm(this, form)

        session.flush()
        session.commit()

    #---------------------------------------------------------------------------


# ==============================================================================

