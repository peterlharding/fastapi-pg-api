# encoding: utf-8
#
# DB Version: 0.8.25
#       Date: 2020-11-03
#
# -----------------------------------------------------------------------------

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    text
)

from sqlalchemy.dialects.postgresql import (
    TIMESTAMP
)


# -----------------------------------------------------------------------------

from .. import app, Base


# =============================================================================
# Session
# -----------------------------------------------------------------------------
"""
# \d session;
                                         Table "public.session"
   Column    |            Type             | Collation | Nullable |               Default
-------------+-----------------------------+-----------+----------+-------------------------------------
 id          | integer                     |           | not null | nextval('session_id_seq'::regclass)
 username    | character varying(32)       |           | not null |
 workstation | character varying(32)       |           | not null |
 started     | timestamp without time zone |           | not null |
 data        | text                        |           |          |
Indexes:
    "session_pkey" PRIMARY KEY, btree (id)
"""
# ----------------------------------------------------------------------------

class Session(Base):

    __tablename__  = 'session'

    id             = Column(Integer, primary_key=True)
    username       = Column(String(32))
    workstation    = Column(String(32))
    data           = Column(Text)
    started        = Column(TIMESTAMP)

    # -------------------------------------------------------------------------

    def __str__(self):
        return '<Session: %r <%s>>' % (self.id, self.username)

    # -------------------------------------------------------------------------

    def __repr__(self):
        return '''\
                <Session: %r>
              Username: %s''' % (self.id, self.username)

    # -------------------------------------------------------------------------

    def jsonify(self):

        return {
                   'id'          : self.id,
                   'username'    : self.username,
                   'workstation' : self.workstation,
                   'data'        : self.data,
                   'started'     : self.started.strftime('%Y-%m-%d %H:%M:%S'),
               }

    # -------------------------------------------------------------------------

    @classmethod
    def SetFromForm(cls, this, form):

        this.username    = form['username']
        this.workstation = form['workstation']

    # -------------------------------------------------------------------------

    @classmethod
    def Save(cls, form):

        id = int(form['id'])

        print('[Session::Save]  Id %d' % id)

        this = Session.query.filter_by(id=id).first()

        Session.SetFromForm(this, form)

        flush()
        commit()

    # -------------------------------------------------------------------------

    @classmethod
    def Add(cls, form, db):

        this = Session()

        Session.SetFromForm(this, form)

        sql = text("SELECT MAX(id) from session")

        try:
            next_id = db.execute(sql).first()[0] + 1
        except:
            next_id = 1

        print('[Session::Add]  next_id %d' % next_id)

        this.id          = next_id

        add(this)

        flush()
        commit()

    # -------------------------------------------------------------------------

    @classmethod
    def NextId(cls, db):

        sql = text("SELECT MAX(id) from session")

        try:
            next_id = db.execute(sql).first()[0] + 1
        except:
            next_id = 1

        return next_id

    # -------------------------------------------------------------------------


# =============================================================================

