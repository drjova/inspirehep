# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.


import pytest
from helpers.providers.faker import faker

from inspirehep.pidstore.minters.base import Minter


def test_pid_value_with_duplicate(base_app, db, create_record_factory):

    arxiv_value_1 = faker.arxiv()
    data = {"arxiv_eprints": [{"value": arxiv_value_1}, {"value": arxiv_value_1}]}
    record = create_record_factory("lit", data=data)
    data = record.json

    minter = Minter(record.id, data)
    minter.pid_value_path = "arxiv_eprints.value"

    expected_len = 1
    expected_value = [arxiv_value_1]

    result_value = minter.get_pid_values()
    result_value_len = len(result_value)

    assert expected_value == result_value
    assert expected_len == result_value_len
