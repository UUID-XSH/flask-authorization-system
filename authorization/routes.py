# coding: utf-8
from datetime import datetime, timedelta

import flask
from authorization import oauth, app, auth, multi_auth
from authorization.alchemy_encoder import AlchemyEncoder
from authorization.models import User, db, Company
from flask import jsonify, g
import uuid


@app.route('/', methods=['GET'])
def home():
    return "welcome to credit block chain authorization server"


@app.route('/company', methods=['GET'])
def list_company():
    return jsonify(flask.json.dumps(Company.query.all(), cls=AlchemyEncoder, ensure_ascii=False))


@oauth.verify_token
def verify_token(token):
    user = User.query.filter_by(token=token).first()
    if not user:
        return False
    if user.expire_time < datetime.now():
        return False
    g.current_user = user
    return True


@auth.verify_password
def verify_password(username, password):
    # try to authenticate with username/password
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    g.current_user = user
    return True


@app.route('/oauth/token', methods=['POST'])
@auth.login_required
def access_token():
    g.current_user.token = str(uuid.uuid4())
    g.current_user.expire_time = datetime.now() + timedelta(minutes=30)  # token 30 need refresh
    db.session.commit()
    return g.current_user.token


@app.route('/me')
@multi_auth.login_required
def me():
    return jsonify(flask.json.dumps(g.current_user, cls=AlchemyEncoder, ensure_ascii=False))
