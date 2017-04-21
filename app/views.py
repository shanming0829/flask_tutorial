# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from flask import render_template, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required

from app import app, lm
from app.forms import LoginUserForm
from app.models import User

__authors__ = "Shanming Liu"


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginUserForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        if verify_user_info(form.username.data, form.password.data):
            return after_login(form)
    return render_template('login_user.html',
                           title='Sign In',
                           form=form
                           )


def verify_user_info(username, password):
    db_user = User.query.filter_by(username=username).first()
    if db_user.password == password:
        return True
    return False


def after_login(form):
    user = User.query.filter_by(username=form.username.data).first()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
