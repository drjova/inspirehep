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
from inspire_utils.name import generate_name_variations, ParsedName


def test_abstracts_with_sources():
    abstract_value_1 = faker.sentence()
    abstract_value_2 = faker.sentence()
    abstracts = {
        "abstracts": [
            {"value": abstract_value_1, "source": "arxiv"},
            {"value": abstract_value_2, "source": "elsevier"},
        ]
    }
    data = faker.record(data=abstracts)

    data_expected = [
        {
            "value": abstract_value_1,
            "source": "arxiv",
            "abstract_source_suggest": {"input": "arxiv"},
        },
        {
            "value": abstract_value_2,
            "source": "elsevier",
            "abstract_source_suggest": {"input": "elsevier"},
        },
    ]
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["abstracts"]


def test_abstracts_without_source():
    abstract_value_1 = faker.sentence()
    abstracts = {"abstracts": [{"value": abstract_value_1}]}
    data = faker.record(data=abstracts)

    data_expected = [{"value": abstract_value_1}]
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["abstracts"]


def test_abstracts_empty():
    data = faker.record()

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert "abstracts" not in data_result


def test_earliest_date_from_preprint_date():
    date_value = faker.date()

    data = {"preprint_date": date_value}
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["earliest_date"]


def test_earliest_date_from_thesis_info_date():
    date_value = faker.year()

    data = {"thesis_info": {"date": date_value}}
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["earliest_date"]


def test_earliest_date_from_thesis_info_defense_date():
    date_value = faker.date()

    data = {"thesis_info": {"defense_date": date_value}}
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["earliest_date"]


def test_earliest_date_from_publication_info_year():
    date_value = faker.year()

    data = {"publication_info": [{"year": int(date_value)}]}
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["earliest_date"]


def test_earliest_date_from_legacy_creation_date():
    date_value = faker.date()

    data = {"legacy_creation_date": date_value}
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["earliest_date"]


def test_earliest_date_from_imprints_date():
    date_value = faker.date()

    data = {"imprints": [{"date": date_value}]}
    data = faker.record(data=data)

    data_expected = date_value
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["earliest_date"]


def test_earliest_date_empty():

    data = faker.record()
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert "earliest_date" not in data_result


def test_author_count():
    data = {
        "authors": [
            {"full_name": "Smith, John", "inspire_roles": ["author"]},
            {"full_name": "Rafelski, Johann", "inspire_roles": ["author", "editor"]},
            {"full_name": "Rohan, George", "inspire_roles": ["author", "supervisor"]},
        ]
    }
    data = faker.record(data=data)
    data_expected = 2

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["author_count"]


def test_author_count_empty():
    data = faker.record()
    data_expected = 0

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["author_count"]


test_data_authors_full_names_unicode_normized = [
    ({"authors": [{"full_name": "Müller, J."}]}, "müller, j."),
    ({"authors": [{"full_name": "Muller, J."}]}, "muller, j."),
]


@pytest.mark.parametrize(
    "data_authors,data_expected", test_data_authors_full_names_unicode_normized
)
def test_authors_full_name_unicode_normized(data_authors, data_expected):
    data = faker.record(data=data_authors)

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    data_results_fullname_unicode_normalized = data_result["authors"][0][
        "full_name_unicode_normalized"
    ]
    assert data_expected == data_results_fullname_unicode_normalized


test_data_authors_name_variations = [
    (
        {"authors": [{"full_name": "Müller, J."}]},
        generate_name_variations("Müller, J."),
    ),
    (
        {"authors": [{"full_name": "Muller, J."}]},
        generate_name_variations("Muller, J."),
    ),
]


@pytest.mark.parametrize(
    "data_authors,data_expected", test_data_authors_name_variations
)
def test_authors_name_variations_and_suggest(data_authors, data_expected):
    data = faker.record(data=data_authors)

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    data_results_name_variations = data_result["authors"][0]["name_variations"]
    data_results_name_suggest = data_result["authors"][0]["name_suggest"]["input"]

    assert data_expected == data_results_name_variations
    assert data_expected == data_results_name_suggest


def test_authors_empty():
    data = faker.record()

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert "authors" not in data_result


def test_inspire_document_type_from_document_type():
    data = {"document_type": ["thesis"]}
    data = faker.record(data=data)

    data_expected = ["thesis"]
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["facet_inspire_doc_type"]


def test_inspire_document_type_from_refereed():
    data = {"document_type": ["article"], "refereed": True}
    data = faker.record(data=data)

    data_expected = ["article", "peer reviewed"]
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["facet_inspire_doc_type"]


def test_inspire_document_type_from_publication_type():
    data = {"document_type": ["article"], "publication_type": ["introductory"]}
    data = faker.record(data=data)

    data_expected = ["article", "introductory"]
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["facet_inspire_doc_type"]


def test_number_of_references():
    data = {"references": [{"reference": {"label": "1"}}]}
    data = faker.record(data=data)

    data_expected = 1
    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert data_expected == data_result["number_of_references"]


def test_number_of_references_empty():
    data = faker.record()

    schema = LiteratureEnhancedSchema()
    data_result = schema.dump(data).data

    assert "number_of_references" not in data_result
