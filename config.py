import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/scrum'
SQLALCHEMY_TRACK_MODIFICATIONS = True

del os