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

from sqlalchemy.orm import Session

from json import JSONDecodeError


# -----------------------------------------------------------------------------

from .. import app, get_db
from ..auth.bearer import JWTBearer

from ..models import (
    State
)


# =============================================================================

@app.get("/states", tags=["state"])
async def get_all_states(db: Session = Depends(get_db)):
    rows = db.query(State).all()
    return [row.jsonify() for row in rows]


# ------------------------------------------------------------------------------

@app.get("/states/{id}", tags=["state"])
async def get_user_details(id: int, db: Session = Depends(get_db)):
    row = db.query(State).filter_by(id=id).first()
    if row:
        return row.jsonify()
    else:
        return{"msg": "Not found"}


# ------------------------------------------------------------------------------

