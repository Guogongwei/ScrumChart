import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql://XXX:XXX@localhost:3306/XXX
SQLALCHEMY_TRACK_MODIFICATIONS = True

del os