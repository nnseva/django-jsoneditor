AUTHOR = 'Vsevolod Novikov'
AUTHOR_EMAIL = 'nnseva@gmail.com'
URL = 'https://github.com/nnseva/django-jsoneditor'

import jsoneditor

from setuptools import setup, find_packages

description = 'Django JSON Editor'

with open('README.rst') as f:
    long_description = f.read()

setup(
    name = 'django-jsoneditor',
    version = jsoneditor.__version__,
    description = description,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    long_description = long_description,
    packages = [
        'jsoneditor',
        'jsoneditor.fields'
    ],
    package_data = {
        'jsoneditor':[
            'static/jsoneditor/*.js',
            'static/jsoneditor/*.css',
            'static/jsoneditor/img/*',
            'static/django-jsoneditor/*.js',
            'static/django-jsoneditor/*.css',
        ]
    },
    include_package_data = True,
    zip_safe = False,
    install_requires=['packaging']
)
