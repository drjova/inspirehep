# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


from __future__ import absolute_import, division, print_function

import pytest
from helpers.providers.faker import faker
from mock import MagicMock, patch

from inspirehep.records.marshmallow.literature import LiteratureEnhancedSchema


def test_abstracts_with_sources():
    abstract_value_1 = faker.sentence()
    abstract_value_2 = faker.sentence()
    abstracts = {
        'abstracts': [
            {
                'value': abstract_value_1,
                'source': 'arxiv',
            },
            {
                'value': abstract_value_2,
                'source': 'elsevier',
            },
        ],
    }
    data = faker.record(data=abstracts)

    expected_data = [
        {
            'value': abstract_value_1,
            'source': 'arxiv',
            'abstract_source_suggest': {
                'input': 'arxiv',
            },
        },
        {
            'value': abstract_value_2,
            'source': 'elsevier',
            'abstract_source_suggest': {
                'input': 'elsevier',
            },
        },
    ]
    schema = LiteratureEnhancedSchema()
    result_data = schema.dump(data).data

    assert expected_data == result_data['abstracts']


def test_abstracts_without_source():
    abstract_value_1 = faker.sentence()
    abstracts = {
        'abstracts': [
            {
                'value': abstract_value_1,
            },
        ],
    }
    data = faker.record(data=abstracts)

    expected_data = [
        {
            'value': abstract_value_1,
        }
    ]
    schema = LiteratureEnhancedSchema()
    result_data = schema.dump(data).data

    assert expected_data == result_data['abstracts']


def test_abstracts_empty():
    data = faker.record()

    schema = LiteratureEnhancedSchema()
    result_data = schema.dump(data).data

    assert None == result_data
