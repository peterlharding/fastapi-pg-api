
#!/usr/bin/env python3
#
#
# -----------------------------------------------------------------------------
"""
  Utility methods

"""
# -----------------------------------------------------------------------------

from fastapi import (
    Depends,
)

from sqlalchemy.orm import Session as DbSession

from datetime import datetime

# -----------------------------------------------------------------------------

from .. import app, get_db

from ..models import (
    Session,
)


# =============================================================================

def log_session(user, ip_addr, db: DbSession):

    session = Session()

    session.username = user.username
    session.workstation = ip_addr
    session.started = datetime.now()
    session.data = user.user_id

    next_id = Session.NextId(db)

    session.id            = next_id

    db.add(session)

    print("[log_session]        ***** About to commit session |")

    try:
        db.flush()
        db.commit()
    except Exception as ex:
        db.rollback()
        app.logger.info("[log_session]          Rolled back after exception |%s|" % ex)
        # return {"result":"failed '%s'" % ex}

# =============================================================================


