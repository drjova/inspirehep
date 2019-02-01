# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Record serializers."""

from __future__ import absolute_import, print_function

from invenio_records_rest.serializers.json import JSONSerializer
from invenio_records_rest.serializers.response import (
    record_responsify,
    search_responsify,
)

from ..marshmallow.literature import LiteratureMetadataSchemaV1

literature_json_v1 = JSONSerializer(LiteratureMetadataSchemaV1)

literature_json_v1_response = record_responsify(literature_json_v1, "application/json")
literature_json_v1_response_search = search_responsify(
    literature_json_v1, "application/json"
)
