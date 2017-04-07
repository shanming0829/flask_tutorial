# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID

__authors__ = "Shanming Liu"

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

lm = LoginManager(app)
lm.login_view = 'login'
oid = OpenID(app, app.config['OPENID_TMP'])

from app import views
from app import models
