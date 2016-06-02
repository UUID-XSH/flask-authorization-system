# -*- coding:utf-8 -*-
from datetime import datetime
from authorization.models import User, Company
from authorization import db


def setup():
    for c in Company.query.all():
        db.session.delete(c)
    db.session.commit()
    c = Company()
    c.company = "上海凯岸"
    c.create_time = datetime.now()
    c.domain = "http://madailicai.com"
    c.name = "麻袋理财"
    c.role = "MEMBER"
    c.short_mark = "MDLC"

    db.session.add(c)

    for u in User.query.all():
        db.session.delete(u)
    db.session.commit()
    u = User()
    u.company = c
    u.username = "test"
    u.hash_password('test')

    db.session.add(u)
    db.session.commit()
