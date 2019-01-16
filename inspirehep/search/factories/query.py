# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


from __future__ import absolute_import, division, print_function

from elasticsearch_dsl import Q

import inspire_query_parser


def inspire_query_factory():
    """Create an Elastic Search DSL query instance using the generated Elastic Search query by the parser."""

    def inspire_query(query_string, search):
        return Q(inspire_query_parser.parse_query(query_string))

    return inspire_query