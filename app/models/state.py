# encoding: utf-8

from sqlalchemy import (
    Column,
    Integer,
    String,
)


# -----------------------------------------------------------------------------

from .. import app, Base


# ==============================================================================
"""
"""
# -----------------------------------------------------------------------------

class State(Base):

    __tablename__ = 'state'

    id            = Column(Integer, primary_key=True)
    name          = Column(String(64))
    state_code    = Column(String(3))
    country_code  = Column(String(2))

    # ---------------------------------------------------------------------

    def __str__(self):
         return "%3d  %s" % (self.id, self.name)

    # ---------------------------------------------------------------------

    def __repr__(self):
         return "%3d  %s" % (self.id, self.name)

    # ---------------------------------------------------------------------

    def jsonify(self):
         return {
                    'id'          : self.id,
                    'name'        : self.name,
                    'stateCode'   : self.state_code,
                    'countryCode' : self.country_code,
                }

    # ---------------------------------------------------------------------


# =============================================================================

