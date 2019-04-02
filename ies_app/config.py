import os

basedir = os.path.abspath(os.path.dirname(__file__))  #текущий путь 

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'ies_1.db') #текущий путь где находится БД