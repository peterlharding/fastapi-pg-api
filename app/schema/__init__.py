#!/usr/bin/env python3
#
# -----------------------------------------------------------------------------
"""
  Specify schema structure under here


  Automagically convert python SnakeCase to CamelCase:

    * https://medium.com/analytics-vidhya/camel-case-models-with-fast-api-and-pydantic-5a8acb6c0eee

"""
# -----------------------------------------------------------------------------

from datetime import date
from humps import camelize

from pydantic import (
    BaseModel,
    EmailStr,
    Field
)

# -----------------------------------------------------------------------------

def to_camel(string):
    return camelize(string)

# =============================================================================

class CamelCaseModel(BaseModel):
    class Config:
        alias_generator = to_camel
        allow_population_by_field_name = True

# =============================================================================

class PayloadUpdateSchema(CamelCaseModel):

    id              : int
    name            : str
    # ...
    group_mnem      : str

# =============================================================================

class PayloadInsertSchema(CamelCaseModel):

    name            : str
    # ...
    group_mnem      : str


# =============================================================================

from . import user
from . import application_user


# -----------------------------------------------------------------------------

