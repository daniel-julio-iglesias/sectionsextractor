#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    sample use
    >>> from microblog import app
    >>> app.config['SECRET_KEY']
    'you-will-never-guess'
    
TODO: If behind proxy, set your proxy in this file
    
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-you-will-never-guess#1'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # HTTP_PROXY = os.environ.get('HTTP_PROXY') or 'http://user:pass@proxyAddress:proxyPort'
    # HTTPS_PROXY = os.environ.get('HTTPS_PROXY') or 'http://user:pass@proxyAddress:proxyPort0'
    # TODO: If behind proxy, set your proxy
    # HTTP_PROXY = os.environ.get('HTTP_PROXY') or 'http://proxycom:8080'
    # HTTPS_PROXY = os.environ.get('HTTPS_PROXY') or 'http://proxycom:8080'
    HTTP_PROXY = os.environ.get('HTTP_PROXY') or 'http://www-proxy.com:80'
    HTTPS_PROXY = os.environ.get('HTTPS_PROXY') or 'http://www-proxy.com:80'
