import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'development key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://michael:p?fg[7SE@localhost/app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PER_PAGE = 30
    ADMINS = ['michael@crawford.io']
