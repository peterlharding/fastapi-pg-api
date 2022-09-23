#!/usr/bin/env python3
#
#
# -----------------------------------------------------------------------------
"""
"""
# -----------------------------------------------------------------------------

from typing import Union


# -----------------------------------------------------------------------------

from .. import app, get_db
from ..auth.bearer import JWTBearer


# =============================================================================
# Default
# -----------------------------------------------------------------------------

@app.get("/hello-world")
def simple_hello_world_route():
    return {"Hello": "World"}


# -----------------------------------------------------------------------------

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# ------------------------------------------------------------------------------

