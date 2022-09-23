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

from pydantic import BaseModel


# -----------------------------------------------------------------------------

from .. import app
from .. import get_db

from ..auth.bearer import JWTBearer

from ..schema import application_user

from ..models import (
    ApplicationUser
)

# =============================================================================
# This is really User - SEE BELOW
#===============================================================================
"""
# \d application_user
                                        Table "public.application_user"
   Column   |            Type             | Collation | Nullable |                Default
------------+-----------------------------+-----------+----------+---------------------------------------
 id         | integer                     |           | not null | nextval("user_info_id_seq"::regclass)
 user_id    | character varying(64)       |           | not null |
 username   | character varying(45)       |           | not null |
 password   | character(64)               |           | not null |
 email      | character varying(45)       |           | not null |
 first_name | character varying(45)       |           | not null |
 last_name  | character varying(45)       |           | not null |
 created    | timestamp without time zone |           | not null |
 modified   | timestamp without time zone |           | not null |
 last_login | timestamp without time zone |           | not null |
Indexes:
    "application_user_pkey" PRIMARY KEY, btree (id)

"""
# -----------------------------------------------------------------------------

class ApplicationUserInsertSchema(BaseModel):
    """
      Insert ApplicationUser
    """
    username     : str
    firstName    : str
    lastName     : str
    email        : str
    password     : str
    active       : bool
    notes        : str
    currentGroup : str
    role         : str


#------------------------------------------------------------------------------

class ApplicationUserUpdateSchema(BaseModel):
    """
      Update ApplicationUser
    """
    username     : str
    firstName    : str
    lastName     : str
    email        : str
    password     : str
    active       : bool
    notes        : str
    currentGroup : str
    role         : str


# ------------------------------------------------------------------------------

@app.get("/application-users", dependencies=[Depends(JWTBearer())], tags=["user"])
async def get_all_application_users(db: Session = Depends(get_db)):
    rows = db.query(ApplicationUser).order_by(ApplicationUser.username).all()
    return [row.jsonify() for row in rows]

# ------------------------------------------------------------------------------

@app.get("/application-users/{id}", dependencies=[Depends(JWTBearer())], tags=["user"])
async def get_application_user_by_id(db: Session = Depends(get_db), id: int = None):

    if id:
        row = db.query(ApplicationUser).filter_by(id=id).first()

        if row:
            return row.jsonify()
        else:
            return {"message": "not found"}

    return {"message": "not found"}

# ------------------------------------------------------------------------------

@app.get("/users", dependencies=[Depends(JWTBearer())], tags=["user"])
async def get_users(db: Session = Depends(get_db),
                    id: int = None,
                    user_id: str = None,
                    email: str = None,
                    username: str = None):

    # user_id  = request.args.get("user_id", None)
    # email    = request.args.get("email", None)
    # username = request.args.get("username", None)

    app.logger.info("[get_user_info]                                 id |%s|" % id)
    app.logger.info("[get_user_info]                            user_id |%s|" % user_id)
    app.logger.info("[get_user_info]                              Email |%s|" % email)
    app.logger.info("[get_user_info]                           UserName |%s|" % username)

    if id or user_id or username or email:
        row = None
        if id:
            row = db.query(ApplicationUser).filter_by(id=id).first()
            # app.logger.info("[Users:get]                                    row |%s|" % row)

        elif user_id:
            row = db.query(ApplicationUser).filter_by(user_id=user_id).first()
            # app.logger.info("[Users:get]                                    row |%s|" % row)

        elif username:
            row = db.query(ApplicationUser).filter_by(username=username).first()

        elif email:
            row = db.query(ApplicationUser).filter_by(email=email).first()

        if row:
            return row.jsonify()
        else:
            return {"msg": "no data"}

    else:
        rows = db.query(ApplicationUser).order_by(ApplicationUser.username).all()

    return [row.jsonify() for row in rows]
 

# -----------------------------------------------------------------------------

@app.post("/application-users", dependencies=[Depends(JWTBearer())], tags=["user"])
async def post_application_user(json_data: ApplicationUserInsertSchema, request: Request,
                               db: Session = Depends(get_db)):

    app.logger.info("[Users:post]                             JSON data |%s|" % json_data)

    try:
        user_id         = json_data["user_id"]
    except:
        user_id         = "xyzzy"

    app.logger.info("[Users:post]                                UserId |%s|" % user_id)

    try:
        username        = json_data["username"]
    except:
        username        = "xyzzy"

    try:
        first_name      = json_data["firstName"]
    except:
        first_name      = ""

    try:
        last_name       = json_data["lastName"]
    except:
        last_name       = ""

    try:
        email           = json_data["email"]
    except:
        email           = ""

    try:
        password        = json_data["password"]
    except:
        password        = "Testing-2020"

    try:
        active          = json_data["active"]
    except:
        active          = True

    try:
        notes           = json_data["notes"]
    except:
        notes           = ""

    try:
        current_group   = json_data["currentGroup"]
    except:
        current_group   = "sms"

    try:
        role          = json_data["role"]
    except:
        role          = "guest"

    if not username or not first_name or not last_name or not email:
        return {"result": "Not all required data provided!"}

    # Has this username been used before?  Check email too?

    existing_user = db.query(ApplicationUser).filter_by(username=username).first()

    if existing_user:
        return {"result":"User already exists"}

    # Pick a unique GUID

    guid = str(uuid.uuid4())

    while True:
        existing_user = db.query(ApplicationUser).filter_by(user_id=guid).first()

        if not existing_user:
            break
        else:
            guid = str(uuid.uuid4())

    user               = ApplicationUser()

    hasher             = hashlib.sha256()

    pw                 = password.encode("utf-8")

    app.logger.info("[Users:post]                                    pw |%s|" % pw)

    hasher.update(pw)

    hashed_new         = hasher.hexdigest()

    app.logger.info("[Users:post]                            hashed_new |%s|" % hashed_new)

    id                 = ApplicationUser.NextId()

    app.logger.info("[Users:post]                                    id |%s|" % id)
    app.logger.info("[Users:post]                                  guid |%s|" % guid)

    user.id            = id
    user.user_id       = guid
    user.username      = username
    user.first_name    = first_name
    user.last_name     = last_name
    user.email         = email
    user.password      = hashed_new
    user.active        = active
    user.notes         = notes
    user.current_group = current_group
    user.role          = role
    user.last_login    = user.created = user.modified = datetime.now()

    db.session.add(user)

    db.session.flush()
    db.session.commit()

    return user.jsonify()


# -----------------------------------------------------------------------------

@app.put("/application-users/{id}", dependencies=[Depends(JWTBearer())], tags=["user"])
async def put_application_user(id: int,
                               json_data: ApplicationUserUpdateSchema,
                               db: Session = Depends(get_db)):

    app.logger.info("[Users:put]                                     Id |%s|" % id)

    app.logger.info("[Users:put]                              JSON data |%s|" % json_data)

    try:
        username       = json_data["username"]
    except:
        username       = None

    try:
        first_name     = json_data["firstName"]
    except:
        first_name     = None

    try :
        last_name     = json_data["lastName"]
    except:
        last_name     = None

    try:
        email         = json_data["email"]
    except:
        email         = None

    try:
        active        = json_data["active"]
    except:
        active        = None

    try:
        notes         = json_data["notes"]
    except:
        notes         = None

    try:
        current_group = json_data["currentGroup"]
    except:
        current_group = None

    try:
        role          = json_data["role"]
    except:
        role          = None

    user = ApplicationUser.query.filter_by(id=id).first()

    if username and username != user.username:
         user.username      = username

    if first_name and first_name != user.first_name:
         user.first_name    = first_name

    if last_name and last_name != user.last_name:
         user.last_name     = last_name

    if email and email != user.email:
         user.email         = email

    if active:
         user.active        = active

    if notes:
         user.notes         = notes

    if current_group:
         user.current_group = current_group

    if role:
         user.role          = role

    user.modified = datetime.now()

    db.session.flush()
    db.session.commit()

    return {"result":"success", "id": user.id}


# -----------------------------------------------------------------------------

@app.patch("/application-users/{id}", dependencies=[Depends(JWTBearer())], tags=["user"])
async def patch_application_user(id: int,
                                 json_body: ApplicationUserUpdateSchema,
                                 db: Session = Depends(get_db)):

    app.logger.info("[Users:patch]                            JSON data |%s|" % json_data)

    try:
        username      = json_data["username"]
    except:
        username      = None

    try:
        first_name    = json_data["firstName"]
    except:
        first_name    = None

    try:
        last_name     = json_data["lastName"]
    except:
        last_name     = None

    try:
        email         = json_data["email"]
    except:
        email         = None

    try:
        password      = json_data["password"]
    except:
        password      = None

    try:
        new_password  = json_data["newPassword"]
    except:
        new_password  = None

    try:
        active        = json_data["active"]
    except:
        active        = None

    try:
        notes         = json_data["notes"]
    except:
        notes         = None

    try:
        current_group = json_data["currentGroup"]
    except:
        current_group = None

    try:
        role          = json_data["role"]
    except:
        role          = None

    user = db.query(ApplicationUser).filter_by(id=id).first()

    if username:
         user.username   = username

    if last_name:
         user.last_name  = last_name

    if first_name:
         user.first_name = first_name

    if email:
         user.email      = email

    if active:
         user.active     = active

    if notes:
         user.notes      = notes

    if current_group:
         user.current_group = current_group

    if role:
         user.role       = role

    if new_password and len(new_password) > 0:

        hasher           = hashlib.sha256()

        pw               = new_password.encode("utf-8")

        app.logger.info("[Users:patch]                                   pw |%s|" % pw)

        hasher.update(pw)

        hashed_new       = hasher.hexdigest()

        user.password = hashed_new

    user.modified = datetime.now()

    db.session.flush()
    db.session.commit()

    return {"result":"success", "id": user.id, "userId": user.user_id}


# -----------------------------------------------------------------------------

@app.delete("/appliocation-users/{user_id}", dependencies=[Depends(JWTBearer())], tags=["user"])
async def delete(user_id: str,
                 db: Session = Depends(get_db)):

    app.logger.info("[Users:delete[                              UserId |%s|" % user_id)

    user = db.query(ApplicationUser).filter_by(user_id=user_id).first()

    if user:

        db.session.delete(user)
        db.session.commit()

        return {"result":"success"}

    else:

        return {"result": "Not found"}, 404


# =============================================================================

@app.get("/users/userid/{user_id}", dependencies=[Depends(JWTBearer())], tags=["user"])
async def get_user_guid(user_id=None,
                       db: Session = Depends(get_db)):
    """
      Note:  user_id is a GUID!
    """

    app.logger.info("[ApplicationUser:get]                              UserId |%s|" % user_id)

    if user_id is None:
        rows = db.query(ApplicationUser).order_by(ApplicationUser.username).all()
        return [row.jsonify() for row in rows]
    else:

        app.logger.info("[ApplicationUser:get]                Querying User UserId |%s|" % user_id)

        row = db.query(ApplicationUser).filter_by(user_id=user_id).first()

        app.logger.info("[ApplicationUser:get]                                 row |%s|" % row)

    if row:
        return row.jsonify()
    else:
        return {"message":f"No user found for user - {user_id}"}


# =============================================================================

@app.get("/users/id/{id}", dependencies=[Depends(JWTBearer())], tags=["user"])
async def get_user_by_id(id: int = None,
                         db: Session = Depends(get_db)):
    """
      Note:  id is the DB index and an integer
    """

    app.logger.info("[ApplicationUser:get]                                  Id |%s|" % id)

    if id is None:
        rows = db.query(ApplicationUser).order_by(ApplicationUser.username).all()
        return [row.jsonify() for row in rows]
    else:

        app.logger.info("[ApplicationUser:get]                Querying User by  Id |%s|" % id)

        row = db.query(ApplicationUser).filter_by(id=id).first()

        app.logger.info("[ApplicationUser:get]                                 row |%s|" % row)

        if row:
            return row.jsonify()
        else:
            return {"message":f"No user found for user - {id}"}

# =============================================================================

