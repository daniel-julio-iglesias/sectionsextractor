#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    sample use
    >>> from microblog import app
    >>> app.config['SECRET_KEY']
    'you-will-never-guess'
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

http_proxy = app.config['HTTP_PROXY']
https_proxy = app.config['HTTPS_PROXY']

from app import routes, models
