# -*- coding:utf-8 -*-

from passlib.apps import custom_app_context as pwd_context

if __name__ == '__main__':
    password = 123
    while password != 'EXIT':
        password = input("please input password (EXIT quit): ")
        print("password is %s" % (pwd_context.encrypt(password)))
