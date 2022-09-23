#!/usr/bin/env python3
#
#
# -----------------------------------------------------------------------------
"""
"""
# -----------------------------------------------------------------------------

from typing import Union

from fastapi import (
    Depends,
    Request,
    status,
    HTTPException
)

from sqlalchemy import func

from sqlalchemy.orm import Session

from json import JSONDecodeError


# -----------------------------------------------------------------------------

from .. import app, get_db
from ..auth.bearer import JWTBearer

from ..models import (
    City
)


# =============================================================================

@app.get("/cities", tags=["city"])
async def get_all_cities(stateCode: Union[str, None] = None,
                          countryCode: Union[str, None] = None,
                          db: Session = Depends(get_db)):
    if stateCode:
        rows = db.query(City).filter(func.lower(City.state_code) == func.lower(stateCode)).all()
    elif countryCode:
        rows = db.query(City).filter(func.lower(City.country_code) == func.lower(countryCode)).all()
    else:
        rows = db.query(City).all()
    return [row.jsonify() for row in rows]


# ------------------------------------------------------------------------------

@app.get("/cities/{id}", tags=["city"])
async def get_user_details(id: int, db: Session = Depends(get_db)):
    row = db.query(City).filter_by(id=id).first()
    if row:
        return row.jsonify()
    else:
        return{"msg": "Not found"}


# ------------------------------------------------------------------------------

