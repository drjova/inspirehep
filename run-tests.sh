#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

# Ignoring flask-admin XSS vulnerability 36437, remove when
# https://github.com/flask-admin/flask-admin/pull/1699 is merged an released.
pipenv check --ignore 36437 && \
pipenv run pydocstyle inspirehep tests docs && \
pipenv run isort -rc -c -df && \
pipenv run check-manifest --ignore ".travis-*,docs/_build*" && \
pipenv run sphinx-build -qnNW docs docs/_build/html && \
pipenv run test
