# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__authors__ = "Shanming Liu"

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import views
from app import models
