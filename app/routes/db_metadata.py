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
    DbMetadata
)

# =============================================================================

@app.get("/db-metadata", tags=["system-metadata"])
async def get_db_metadata(db: Session = Depends(get_db)):
    row = db.query(DbMetadata).first()
    return row.jsonify()

# ------------------------------------------------------------------------------

@app.get("/db-version", tags=["system-metadata"])
async def get_db_version(db: Session = Depends(get_db)):
    row = db.query(DbMetadata).first()
    return {"dbVersion" : row.db_version}

# ------------------------------------------------------------------------------

@app.get('/app-version', tags=["system-metadata"])
async def get_app_version(db: Session = Depends(get_db)):
    return {"version" : app.__version__}

# ------------------------------------------------------------------------------

