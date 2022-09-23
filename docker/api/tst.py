#!/usr/bin/env python3

import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from CONFIG import (
    DBUser,
    DBPassword,
    DBName,
    URI_TEMPLATE,
)

DBHost             = 'localhost:5433'

# -----------------------------------------------------------------------------
# Let's connect explicitly to FastAPI Database
# -----------------------------------------------------------------------------

uri = URI_TEMPLATE  % (DBUser, DBPassword, DBHost, DBName)

print(f"URL |{uri}|")

engine = create_engine(uri)

unbound_session = sessionmaker()

session = unbound_session(bind=engine)

# -----------------------------------------------------------------------------

results = session.execute('SELECT * FROM application_user')

for result in results:
    print(result)

