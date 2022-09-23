#!/usr/bin/env python3
#
#
#
# -----------------------------------------------------------------------------
"""
    Main component of app
"""
# -----------------------------------------------------------------------------

import jwt
import uuid
import urllib

from datetime import datetime

from typing import (
    Dict,
    List,
    Optional,
    Union
)

from fastapi import (
    FastAPI,
    Body,
    Depends,
    Request,
    status,
    HTTPException
)

from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import (
    RedirectResponse,
    HTMLResponse
)


from starlette.responses import RedirectResponse

from sqlalchemy.orm import Session

from decouple import config


# -----------------------------------------------------------------------------

from . import app, routes

from .schema.user import (
    UserLoginSchema,
    UserSchema,
)

from .auth.handler import sign_token
from .auth.bearer import JWTBearer


# -----------------------------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.JWT_SECRET    = config("secret")
app.JWT_ALGORITHM = config("algorithm")


# =============================================================================




