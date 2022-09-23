#!/usr/bin/env python3
#
#
#
# -----------------------------------------------------------------------------
"""
    Main component of app
"""
# -----------------------------------------------------------------------------

import time

from fastapi import (
    Depends,
    Request,
    HTTPException
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from sqlalchemy.orm import Session


# -----------------------------------------------------------------------------

from .. import app, SessionLocal

from ..models import (
    ApplicationUser,
    TokenBlacklist,
)

from .handler import sign_token, decode_token


# =============================================================================
# Handle Bearer Tokens
# -----------------------------------------------------------------------------

class JWTBearer(HTTPBearer):

    # -------------------------------------------------------------------------

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    # -------------------------------------------------------------------------

    async def __call__(self, request: Request):

        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)

        if credentials:

            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")

            if not self.verify_token(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")

            return credentials.credentials

        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    # -------------------------------------------------------------------------

    def verify_token(self, token: str) -> bool:

        # Check to see if token is blacklisted

        try:
            is_blacklisted_token = TokenBlacklist.check_blacklist(token)
            if is_blacklisted_token:
                raise HTTPException(status_code=401, detail="Token blacklisted. Please log in again.")

        except Exception as ex:
            app.logger.info("[verify_token]  Blacklist check failed -        ex |%s|" % ex)
            raise HTTPException(status_code=401, detail="Blacklist Token check failed.")

        db: Session = SessionLocal()

        is_valid: bool = False

        try:
            payload = decode_token(token)

        except:
            app.logger.info("[verify_token]  Signature verification failed - ex |%s|" % ex)
            raise HTTPException(status_code=401, detail="Signature verification failed.")

        print(payload)

        subject = payload['sub']
        expires = payload['exp']

        now = int(time.time())

        if expires < now:
            app.logger.info("[verify_token]                  Token expired - ex |%s|" % ex)
            raise HTTPException(status_code=401, detail="Token expired")

        user = db.query(ApplicationUser).filter_by(user_id=subject).first()

        if user:
            is_valid = True
        else:
            app.logger.info("[verify_token]               Not a valid user - ex |%s|" % ex)
            raise HTTPException(status_code=401, detail="Not a valid user")

        return is_valid

    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------

