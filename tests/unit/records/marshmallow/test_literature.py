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

    data_expected = [
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
    data_result = schema.dump(data).data

    assert data_expected == data_result['abstracts']


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

    data_expected = [
        {
            'value': abstract_value_1,
        }
    ]
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['abstracts']


def test_abstracts_empty():
    data = faker.record()

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert 'abstracts' not in data_result


def test_earliest_date_from_preprint_date():
    date_value = faker.date()

    data = {
        'preprint_date': date_value,
    }
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['earliest_date']


def test_earliest_date_from_thesis_info_date():
    date_value = faker.year()

    data = {
        'thesis_info': {
            'date': date_value,
        },
    }
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['earliest_date']


def test_earliest_date_from_thesis_info_defense_date():
    date_value = faker.date()

    data = {
        'thesis_info': {
            'defense_date': date_value,
        },
    }
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['earliest_date']


def test_earliest_date_from_publication_info_year():
    date_value = faker.year()

    data = {
        'publication_info': [
            {
                'year': int(date_value),
            },
        ],
    }
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['earliest_date']


def test_earliest_date_from_legacy_creation_date():
    date_value = faker.date()

    data = {
        'legacy_creation_date': date_value,
    }
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['earliest_date']


def test_earliest_date_from_imprints_date():
    date_value = faker.date()

    data = {
        'imprints': [
            {
                'date': date_value,
            },
        ],
    }
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['earliest_date']


def test_earliest_date_empty():

    data = faker.record()
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert 'earliest_date' not in data_result


def test_author_count():
    data = {
        'authors': [
            {
                'full_name': 'Smith, John',
                'inspire_roles': [
                    'author',
                ],
            },
            {
                'full_name': 'Rafelski, Johann',
                'inspire_roles': [
                    'author',
                    'editor',
                ],
            },
            {
                'full_name': 'Rohan, George',
                'inspire_roles': [
                    'author',
                    'supervisor',
                ],
            },
        ],
    }
    data = faker.record(data=data)
    data_expected = 2

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['author_count']


def test_author_count_empty():
    data = faker.record()
    data_expected = 0

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['author_count']


def authors_full_name_unicode_normalized():
    data = {
        'authors': [
            {
                'full_name': 'Müller, J.',
            },
            {
                'full_name': 'Muller, J.',
            },
        ],
    }
    data = faker.record()

    data_expected = [
        {
            'full_name': u'Müller, J.',
            'full_name_unicode_normalized': u'müller, j.',
        },
        {
            'full_name': u'Muller, J.',
            'full_name_unicode_normalized': u'muller, j.',
        },
    ]
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result['authors']


def authors_full_name_unicode_normalized_empty():
    data = faker.record()

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert 'authors' not in data_result
