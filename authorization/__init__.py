# -*- coding:utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth, MultiAuth
import os

app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.debug = True
app.secret_key = 'secret'

db_url = 'sqlite:///db.sqlite'
if os.environ.get('DB_URL'):
    db_url = os.environ.get('DB_URL')

app.config.update({
    'SQLALCHEMY_DATABASE_URI': db_url,
    'SQLALCHEMY_TRACK_MODIFICATIONS': True
})

db = SQLAlchemy(app)
# = OAuth2Provider(app)
oauth = HTTPTokenAuth(scheme='Token')
auth = HTTPBasicAuth()
multi_auth = MultiAuth(oauth, auth)

import authorization.models
import authorization.routes
# import authorization.init

# init.setup()
