# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Schemas for marshmallow."""

from __future__ import absolute_import, print_function

from inspire_dojson.utils import strip_empty_values
from marshmallow import Schema, post_dump, missing

from .json import RecordSchemaV1


class RecordSchema(Schema):
    @post_dump
    def clean_data(self, data):
        return strip_empty_values(data)
