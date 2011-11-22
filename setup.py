#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

static_files = []
for root, subFolders, files in os.walk("filtrate/static"):
    for f in files:
        path = os.path.join(root, f)
        # Remove 'filtrate/'
        path = path[9:]
        static_files.append(path)

setup(
    name='django-admin-filtrate',
    version='0.1',
    description='This Django app makes it easier to create custom filters in the change list of Django Admin and supplies a TreeFilter and a DateRangeFilter too.',
    author='Rune Kaagaard',
    url='https://github.com/runekaagaard/django-admin-filtrate',
    packages=find_packages(),
    package_data = {'filtrate': ['templates/admin/*'] + static_files },
)