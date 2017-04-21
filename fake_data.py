# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import datetime

from app import db, models

__authors__ = "Shanming Liu"


def add_user():
    user1 = models.User(nickname='john', email='john@email.com')
    user2 = models.User(nickname='susan', email='susan@email.com')

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()


def query_user():
    users = models.User.query.filter_by(username='aaa').first()
    print(users)


def add_post():
    user1 = models.User.query.get(1)
    post = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=user1)
    db.session.add(post)
    db.session.commit()


def clear_all():
    users = models.User.query.all()
    for user in users:
        db.session.delete(user)

    posts = models.Post.query.all()
    for post in posts:
        db.session.delete(post)

    db.session.commit()


def add_user_password():
    user1 = models.User(username='aaa', password='aaa', email='aaa@email.com')
    db.session.add(user1)
    db.session.commit()


if __name__ == '__main__':
    query_user()
