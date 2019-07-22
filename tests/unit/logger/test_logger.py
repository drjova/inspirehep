# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# inspirehep is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

import mock
from flask import Flask

from inspirehep.logger import InspireLogger


def test_ext_without_dsn():
    app = Flask("testapp")
    ext = InspireLogger(app)

    assert "inspirehep-logger" not in app.extensions


@mock.patch("inspirehep.logger.ext.sentry_sdk.init")
def test_ext_with_dsn(mock_sentry_sdk):
    SENTRY_DSN = "TEST_DSN_URL_FOR_SENTRY"
    SENTRY_SEND_DEFAULT_PII = True

    app = Flask("testapp")
    app.config.update(
        {"SENTRY_DSN": SENTRY_DSN, "SENTRY_SEND_DEFAULT_PII": SENTRY_SEND_DEFAULT_PII}
    )
    ext = InspireLogger(app)

    assert "inspirehep-logger" in app.extensions
    mock_sentry_sdk.assert_called_once()
