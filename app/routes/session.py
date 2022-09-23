#!/usr/bin/env python3
#
#
# -----------------------------------------------------------------------------
"""
"""
# -----------------------------------------------------------------------------

from fastapi import (
    Depends,
    Request,
    status,
    HTTPException
)

from sqlalchemy.orm import Session as SqlalchemySession

from json import JSONDecodeError


# -----------------------------------------------------------------------------

from .. import app, get_db
from ..auth.bearer import JWTBearer

from ..models import (
    Session
)


# =============================================================================

@app.get("/sessions", tags=["session"])
async def get_all_sessions(db: SqlalchemySession = Depends(get_db)):
    rows = db.query(Session).all()
    return [row.jsonify() for row in rows]


# ------------------------------------------------------------------------------

@app.get("/sessions/{id}", tags=["session"])
async def get_user_details(id: int, db: SqlalchemySession = Depends(get_db)):
    row = db.query(Session).filter_by(id=id).first()
    if row:
        return row.jsonify()
    else:
        return{"msg": "Not found"}


# ------------------------------------------------------------------------------

