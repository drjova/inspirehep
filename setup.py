# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Inspire"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

INVENIO_VERSION = "3.1.0.dev20181106"

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('inspirehep', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='inspirehep',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='inspirehep Invenio',
    license='MIT',
    author='CERN',
    author_email='info@inspirehep.net',
    url='https://github.com/inspirehep/inspirehep',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'inspirehep = invenio_app.cli:cli',
        ],
        'invenio_base.apps': [
            'flask_debugtoolbar = flask_debugtoolbar:DebugToolbarExtension',
            'inspirehep_records = inspirehep.records:inspirehep',
        ],
        'invenio_base.blueprints': [
            'inspirehep = inspirehep.theme.views:blueprint',
            'inspirehep_records = inspirehep.records.views:blueprint',
        ],
        'invenio_config.module': [
            'inspirehep = inspirehep.config',
        ],
        'invenio_i18n.translations': [
            'messages = inspirehep',
        ],
        'invenio_base.api_apps': [
            'inspirehep = inspirehep.records:inspirehep',
         ],
        'invenio_jsonschemas.schemas': [
            'inspirehep = inspirehep.records.jsonschemas'
        ],
        'invenio_search.mappings': [
            'records = inspirehep.records.mappings'
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 3 - Alpha',
    ],
)
