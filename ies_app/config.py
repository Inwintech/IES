import os

SERVER_IP = '192.168.1.104'
DEVICE_IP = '192.168.1.156'
DEVICE_ID = 127001

basedir = os.path.abspath(os.path.dirname(__file__))  #текущий путь 

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'ies_1.db') #текущий путь где находится БД