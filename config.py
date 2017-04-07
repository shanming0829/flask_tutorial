import os
from util.common import combine_path

basedir = os.path.abspath(os.path.dirname(__file__))

OPENID_TMP = combine_path(basedir, 'tmp')

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + combine_path(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = combine_path(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'},
]
