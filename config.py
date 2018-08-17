""" The MIT License (MIT)

Copyright (c) 2017 Miguel Grinberg

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

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
