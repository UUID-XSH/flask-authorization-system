# coding: utf-8
from authorization import db, app
from authorization import init

if __name__ == '__main__':
    db.create_all()
    init.setup()
    app.run()
