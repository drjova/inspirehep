# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""JSON Schemas."""

from __future__ import absolute_import, print_function

from itertools import chain
from unicodedata import normalize

from invenio_records_rest.schemas import StrictKeysMixin
from invenio_records_rest.schemas.fields import DateString, SanitizedUnicode
from marshmallow import fields, missing, validate
from inspire_utils.date import earliest_date
from inspire_utils.record import get_value
from inspire_utils.helpers import force_list
from inspire_utils.name import generate_name_variations, ParsedName

from . import RecordSchema


class LiteratureSchema(RecordSchema):
    pass


# Enhanced schema is a record we prepare for elasticsearch
class LiteratureEnhancedSchema(RecordSchema):

    abstracts = fields.Method("get_abstracts", dump_only=True)
    authors = fields.Method("get_authors", dump_only=True)
    author_count = fields.Method("get_author_count", dump_only=True)
    earliest_date = fields.Method("get_earliest_date", dump_only=True)
    facet_inspire_doc_type = fields.Method("get_facet_inspire_doc_type", dump_only=True)
    number_of_references = fields.Method("get_number_of_references", dump_only=True)

    @staticmethod
    def normilize_unicode(text):
        return normalize("NFKC", text).lower()

    @staticmethod
    def name_variations(names):
        return generate_name_variations(names)

    def get_abstracts(self, data):
        abstracts = data.get("abstracts", [])
        for abstract in abstracts:
            source = abstract.get("source")
            if source:
                abstract.update({"abstract_source_suggest": {"input": source}})
        return abstracts

    def get_authors(self, data):
        authors = data.get("authors", [])

        for index, author in enumerate(authors):
            full_name = author["full_name"]
            name_variations = LiteratureEnhancedSchema.name_variations(full_name)
            authors[index].update(
                {
                    "full_name_unicode_normalized": LiteratureEnhancedSchema.normilize_unicode(
                        full_name
                    ),
                    "name_variations": LiteratureEnhancedSchema.name_variations(
                        full_name
                    ),
                    "name_suggest": {
                        "input": [
                            variation for variation in name_variations if variation
                        ]
                    },
                }
            )
        return authors

    def get_author_count(self, data):
        authors = data.get("authors", [])

        authors_excluding_supervisors = [
            author
            for author in authors
            if "supervisor" not in author.get("inspire_roles", [])
        ]
        return len(authors_excluding_supervisors)

    def get_earliest_date(self, data):
        date_paths = [
            "preprint_date",
            "thesis_info.date",
            "thesis_info.defense_date",
            "publication_info.year",
            "legacy_creation_date",
            "imprints.date",
        ]

        dates = [
            str(el)
            for el in chain.from_iterable(
                [force_list(get_value(data, path)) for path in date_paths]
            )
        ]

        if dates:
            result = earliest_date(dates)
            if result:
                return result

    def get_facet_inspire_doc_type(self, data):
        result = []

        result.extend(data.get("document_type", []))
        result.extend(data.get("publication_type", []))
        if "refereed" in data and data["refereed"]:
            result.append("peer reviewed")
        return result

    def get_number_of_references(self, data):
        references = data.get("references")

        if references is not None:
            return len(references)
