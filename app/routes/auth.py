#!/usr/bin/env python3
#
#
# -----------------------------------------------------------------------------
"""
"""
# -----------------------------------------------------------------------------

import jwt

from fastapi import (
    Depends,
    Header,
    Request,
    Response,
    status,
    HTTPException
)

from fastapi.security import HTTPBasic, HTTPBasicCredentials

from pydantic import BaseModel
from sqlalchemy.orm import Session as SqaSession
from datetime import datetime, timedelta
from json import JSONDecodeError


# -----------------------------------------------------------------------------

from .. import app, get_db
from ..auth.bearer import JWTBearer
from ..utils import log_session

from ..models import (
    ApiCredentials,
    ApplicationUser,
    Session,
)


# -----------------------------------------------------------------------------

security = HTTPBasic()


# =============================================================================

class DbCredentials(BaseModel):
    username: str
    password: str

# -----------------------------------------------------------------------------

class UserSchema(BaseModel):
  id: int
  userId: str
  username: str
  password: str
  email: str
  firstName: str
  lastName: str
  notes: str
  isAdmin: bool
  lastLogin: datetime
  whenCreated: datetime
  whenModified: datetime


# -----------------------------------------------------------------------------

class AuthPayload(BaseModel):
    token: str
    refreshInterval: int
    user: UserSchema

# =============================================================================

@app.post("/v3/authenticate", response_model=AuthPayload, tags=["auth"])
async def authenticate_v3(
                           body: DbCredentials,
                           request: Request,
                           response: Response,
                           credentials: HTTPBasicCredentials = Depends(security),
                           db: SqaSession = Depends(get_db)):

    app.logger.info("[/v3/authorization]                    credentials |%s|" % credentials)
    print("[/v3/authorization]                    credentials |%s|" % credentials)

    if credentials:

        basic_auth_user = db.query(ApiCredentials).filter_by(email=credentials.username).first()

        # Also need to check password!

        app.logger.info("[/v3/authenticate]                 basic_auth_user |%s|" % basic_auth_user)
        print("[/v3/authenticate]                 basic_auth_user |%s|" % basic_auth_user)

        if basic_auth_user is None:
            raise HTTPException(status_code=401, detail=f"Invalid credentials - {credentials.username}")

        if not basic_auth_user.is_correct_password(credentials.password):
            raise HTTPException(status_code=401, detail="Invalid Basic Auth.")

        try:
            user = db.query(ApplicationUser).filter_by(username=body.username).first()  # Maybe should be UserDetails for consistency with API;
        except Exception as ex:
            db.rollback()
            app.logger.info("[/v3/authenticate]   Rolled back after session query exception |%s|" % ex)
            user = db.query(ApplicationUser).filter_by(username=body.username).first()

        app.logger.info("[v3/authenticate]                             user |%s|" % user)

        if user is None:
            app.logger.info("[/v3/authenticate]       User not found")
            response.status_code = 401
            raise HTTPException(status_code=401, detail="Invalid User.")

        app.logger.info("[/v3/authenticate]     Successfully retrieved user |%s|" % user)
        print("[/v3/authenticate]     Successfully retrieved user |%s|" % user)
        print("[/v3/authenticate]                        Password |%s|" % user.password)

        if not user.is_correct_password(body.password):
            print("[/v3/authenticate]                    BAD password |%s|" % body.password)
            app.logger.info("[/v3/authenticate]                    BAD password |%s|" % body.password)
            response.status_code = 401
            return {"error":"Invalid authentication"}
            raise HTTPException(status_code=401, detail="Invalid authentication.")

        app.logger.info("[/v3/authenticate]             User password is OK |%s|" % user)

        token = jwt.encode({
                              'sub': user.user_id,
                              'iat': datetime.utcnow(),
                              'exp': datetime.utcnow() + timedelta(minutes=60)},
                               app.JWT_SECRET,
                               algorithm=app.JWT_ALGORITHM
                           )

        log_session(user, request.client.host, db)

        return {
                 "token": token,
                 "refreshInterval": 3600,
                 "user": user.jsonify()
               }


# ------------------------------------------------------------------------------

