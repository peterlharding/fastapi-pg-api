
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
import time

from typing import (
    Dict,
)

from datetime import datetime


# -----------------------------------------------------------------------------

from .. import app


# =============================================================================
# AUth Endpoints
# -----------------------------------------------------------------------------

def token_response(token: str):
    return {
        "token": token
    }


# -----------------------------------------------------------------------------

def sign_token(user_id: str) -> Dict[str, str]:
    payload = {
        'sub': user_id,       # user.user_id
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=60)
    }

    # Maybe set expiry period as a secret?

    token = jwt.encode(payload, app.JWT_SECRET, algorithm=app.JWT_ALGORITHM)

    return token_response(token)


# -----------------------------------------------------------------------------

def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, app.JWT_SECRET, algorithms=[app.JWT_ALGORITHM])

    except:
        return {}


# -----------------------------------------------------------------------------

