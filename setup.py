#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    :copyright: (assumed) Copyright 2013 by S. Andrew Sheppard
    :contact: andrew@wq.io
"""


from setuptools import setup


setup(
    name='django-github-patterns',
    version='0.1.0',
    description='Django generic URL patterns',
    long_description="small hack to make URL confs more readable (forked by Hugo Geoffroy to add setup.py)",
    author='S. Andrew Sheppard, Hugo Geoffroy',
    author_email='andrew@wq.io',
    packages = ['github_hook'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
)
