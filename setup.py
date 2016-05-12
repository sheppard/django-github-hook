#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: Copyright 2013-2016 by S. Andrew Sheppard
    :contact: andrew@wq.io
"""


from setuptools import setup
from os.path import join, dirname

LONG_DESCRIPION = """
Webhooks for GitHub post-receive hooks and other POST requests.
"""

def long_description():
    """Return long description from README.rst if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name='django-github-hook',
    version='0.2.0',
    description='Django-powered GitHub (& Bitbucket) web hooks',
    long_description=long_description(),
    author='S. Andrew Sheppard & Contributors',
    author_email='andrew@wq.io',
    packages = ['github_hook'],
    install_requires=['Django', 'djangorestframework'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
    ],
    platforms=['any'],
    test_suite='tests'
)
