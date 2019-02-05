# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

from inspire_dojson.utils import strip_empty_values
from invenio_records_rest.schemas.json import RecordSchemaJSONV1
from marshmallow import Schema, fields, post_dump

# FIXME
from inspirehep.modules.records.utils import get_author_with_record_facet_author_name

from .common import PositionSchemaV1


class AuthorsMetadataSchemaV1(Schema):
    """Schema for Authors records."""

    _collections = fields.Raw(dump_only=True)
    acquisition_source = fields.Raw(dump_only=True)
    advisors = fields.Raw(dump_only=True)
    arxiv_categories = fields.Raw(dump_only=True)
    awards = fields.Raw(dump_only=True)
    birth_date = fields.Raw(dump_only=True)
    control_number = fields.Raw(dump_only=True)
    death_date = fields.Raw(dump_only=True)
    deleted = fields.Raw(dump_only=True)
    email_addresses = fields.Raw(dump_only=True)
    ids = fields.Raw(dump_only=True)
    inspire_categories = fields.Raw(dump_only=True)
    name = fields.Raw(dump_only=True)
    new_record = fields.Raw(dump_only=True)
    positions = fields.Nested(PositionSchemaV1, dump_only=True, many=True)
    should_display_positions = fields.Method("get_should_display_positions")
    project_membership = fields.Raw(dump_only=True)
    status = fields.Raw(dump_only=True)
    stub = fields.Raw(dump_only=True)
    urls = fields.Raw(dump_only=True)
    facet_author_name = fields.Method("get_facet_author_name")

    @staticmethod
    def get_facet_author_name(data):
        if "facet_author_name" not in data:
            return get_author_with_record_facet_author_name(data)
        else:
            return data["facet_author_name"]

    @staticmethod
    def get_should_display_positions(data):
        positions = data.get("positions")

        if positions is None:
            return False

        if len(positions) == 1:
            position = positions[0]

            return position.get("current") is not True or any(
                key in position for key in ["rank", "start_date", "end_date"]
            )

        return True

    @post_dump
    def strip_empty(self, data):
        return strip_empty_values(data)


class AuthorsSchemaV1(RecordSchemaJSONV1):
    metadata = fields.Nested(AuthorsMetadataSchemaV1, dump_only=True)
