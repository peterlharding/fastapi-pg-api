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
    HTTPException,
)

from sqlalchemy import func
from sqlalchemy.orm import Session

from json import JSONDecodeError


# -----------------------------------------------------------------------------

from .. import app, get_db
from ..auth.bearer import JWTBearer

from ..models import (
    ISO_Country
)


# =============================================================================

@app.get("/iso-countries", tags=["iso-country"])
async def get_all_iso_countries(db: Session = Depends(get_db)):
    rows = db.query(ISO_Country).all()
    return [row.jsonify() for row in rows]


# ------------------------------------------------------------------------------

@app.get("/iso-countries/{code}", tags=["iso-country"])
async def get_iso_countries(code: str, db: Session = Depends(get_db)):
    row = db.query(ISO_Country).filter(func.lower(ISO_Country.code)==func.lower(code)).first()
    if row:
        return row.jsonify()
    else:
        return{"msg": "Not found"}


# ------------------------------------------------------------------------------

