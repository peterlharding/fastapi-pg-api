#!/usr/bin/env python3
#
# -------------------------------------------------------------------------------------------------
"""
    Add schema here
"""
# -------------------------------------------------------------------------------------------------

from datetime import date

from pydantic import (
    BaseModel,
    EmailStr,
    Field
)


# -----------------------------------------------------------------------------

"""
MariaDB [contacts]> desc User;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| ID       | int(11)      | NO   | PRI | NULL    | auto_increment |
| Nickname | varchar(64)  | YES  | UNI | NULL    |                |
| Email    | varchar(120) | YES  | UNI | NULL    |                |
| Role     | smallint(6)  | YES  |     | NULL    |                |
| AboutMe  | varchar(140) | YES  |     | NULL    |                |
| LastSeen | datetime     | YES  |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
6 rows in set (0.001 sec)
"""
# -----------------------------------------------------------------------------

class User(BaseModel):
    id:         int
    nickname:   str
    email:      str
    role:       int
    aboutMe:    str


# -----------------------------------------------------------------------------

class UserSchema(BaseModel):
    username: str = Field(...)
    userid:   str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "demo",
                "userid": "eb2c3efc-29a8-4391-b492-d6be19a9e6d5",
                "password": "Some-Password"
            }
        }


# -----------------------------------------------------------------------------

class UserLoginSchema(BaseModel):

    username: str = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "username": "demo",
                "password": "Weak Password"
            }
        }


# -----------------------------------------------------------------------------



