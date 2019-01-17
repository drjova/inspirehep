#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

pipenv check --ignore 36437 --ignore 36759 && \
pipenv run isort -rc -c -df && \
pipenv run check-manifest --ignore ".travis-*,docs/_build*" && \
pipenv run pytest tests/unit
pipenv run pytest tests/integration