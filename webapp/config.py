import os

SERVER_IP = '192.168.0.10'
DEVICE_IP = '192.168.0.90'
DEVICE_ID = 127001

basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')  #указываем где у нас лежит БД