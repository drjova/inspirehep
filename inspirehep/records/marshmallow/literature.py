# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import DateString, SanitizedUnicode
from marshmallow import fields, missing, validate, post_dump

from . import RecordSchema


class LiteratureSchema(RecordSchema):
    pass


# Enhanced schema is a record we prepare for elasticsearch
class LiteratureEnhancedSchema(RecordSchema):

    abstracts = fields.Method('get_abstracts', dump_only=True)

    def get_abstracts(self, data):
        abstracts = data.get('abstracts', [])
        for abstract in abstracts:
            source = abstract.get('source')
            if source:
                abstract.update({
                    'abstract_source_suggest': {
                        'input': source,
                    },
                })
        return abstracts
