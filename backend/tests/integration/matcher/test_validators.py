# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from helpers.utils import create_record

from inspirehep.matcher.validators import authors_validator


def test_authors_validator_match_when_one_identifier_is_duplicated(inspire_app):
    lit_author = {
        "full_name": "Test Author",
        "ids": [{"schema": "WIKIPEDIA", "value": "T.Author.1"}],
    }
    author = {
        "name": {"value": "Test Author"},
        "ids": [
            {"schema": "INSPIRE BAI", "value": "T.Author.1"},
            {"schema": "WIKIPEDIA", "value": "T.Author.1"},
        ],
    }
    record_aut = create_record("aut", data=author)
    assert authors_validator(lit_author, record_aut)


def test_authors_validator_match_when_identifiers_are_duplicated(inspire_app):
    lit_author = {
        "full_name": "Test Author",
        "ids": [
            {"schema": "WIKIPEDIA", "value": "T.Author.1"},
            {"schema": "SPIRES", "value": "T.Author.1"},
        ],
    }
    author = {
        "name": {"value": "Test Author"},
        "ids": [
            {"schema": "INSPIRE BAI", "value": "T.Author.1"},
            {"schema": "WIKIPEDIA", "value": "T.Author.1"},
        ],
    }
    record_aut = create_record("aut", data=author)
    assert authors_validator(lit_author, record_aut)


def test_authors_validator_doesnt_match_when_id_is_from_incorrect_schema(inspire_app,):
    lit_author = {
        "full_name": "Test Author",
        "ids": [
            {"schema": "SPIRES", "value": "T.Author.1"},
            {"schema": "ORCID", "value": "0000-1111-2222-3333"},
        ],
    }
    author = {
        "name": {"value": "Test Author"},
        "ids": [{"schema": "INSPIRE BAI", "value": "T.Author.1"}],
    }
    record_aut = create_record("aut", data=author)
    assert not authors_validator(lit_author, record_aut)


def test_authors_validator_matches_when_id_is_from_correct_schema(inspire_app):
    lit_author = {
        "full_name": "Test Author",
        "ids": [{"schema": "INSPIRE BAI", "value": "T.Author.1"}],
    }
    author = {
        "name": {"value": "Test Author"},
        "ids": [
            {"schema": "INSPIRE BAI", "value": "T.Author.1"},
            {"schema": "SPIRES", "value": "HEPNAMES-400111"},
        ],
    }
    record_aut = create_record("aut", data=author)
    assert authors_validator(lit_author, record_aut)
