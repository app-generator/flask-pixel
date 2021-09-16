# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask    import json

from .models  import Users
from app      import app,db
from flask    import render_template

# build a Json response
def response( data ):
    return app.response_class( response=json.dumps(data),
                               status=200,
                               mimetype='application/json' )
def g_db_commit( ):

    db.session.commit( );    

def g_db_add( obj ):

    if obj:
        db.session.add ( obj )

def g_db_del( obj ):

    if obj:
        db.session.delete ( obj )
