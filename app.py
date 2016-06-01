# coding: utf-8

from authorization import authorization

if __name__ == '__main__':
    authorization.db.create_all()
    authorization.app.run()
