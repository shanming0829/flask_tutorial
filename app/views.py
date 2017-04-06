# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from app import app

__authors__ = "Shanming Liu"


@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"
