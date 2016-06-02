# -*- coding:utf-8 -*-


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider
from flask_httpauth import HTTPTokenAuth, HTTPBasicAuth, MultiAuth

app = Flask(__name__, template_folder="../templates")
app.debug = True
app.secret_key = 'secret'
app.config.update({
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
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
