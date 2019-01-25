# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014-2018 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

from __future__ import absolute_import, division, print_function

import abc
from collections import namedtuple

import six
from flask import current_app

from ..errors import MissingControlNumber, MissingSchema
from ..providers.recid import InspireRecordIdProvider

FetchedPID = namedtuple("FetchedPID", ["provider", "pid_type", "pid_value"])


class PidStoreBase(object):

    pid_type = None
    object_type = "rec"
    minters = []

    @classmethod
    def mint(cls, record_uuid, data):
        for mint in cls.minters:
            mint(record_uuid, data, cls.pid_type, cls.object_type)

    @classmethod
    def fetch(cls, record_uuid, data):
        if "$schema" not in data:
            raise MissingSchema

        if "control_number" not in data:
            raise MissingControlNumber

        return FetchedPID(
            provider=InspireRecordIdProvider,
            pid_type=cls.pid_type,
            pid_value=str(data["control_number"]),
        )

    @staticmethod
    def get_endpoint_from_pid_type(pid_type):
        """Return the ``endpoint`` for a given ``pid_type``.

        Args:
            pid_type (str): the pid_type.

        Returns:
            None if not found, the ``endpoint``.
        """
        pids_to_endpoints = PidStoreBase._get_config_pid_types_to_endpoints()
        return pids_to_endpoints.get(pid_type)

    @staticmethod
    def get_pid_type_from_endpoint(endpoint):
        """Return the ``pid_type`` for a given ``endpoint``.

        Args:
            endpoint (str): the endpoint.
                The entpoint registered for a specicific ``pid_type``,
                for example ``literature``.
        Returns:
            None if not found, the ``pid_type``.
        """
        pids_to_endpoints = PidStoreBase._get_config_pid_types_to_endpoints()
        ENDPOINTS_TO_PID_TYPES = {
            value: key for (key, value) in pids_to_endpoints.items()
        }
        return ENDPOINTS_TO_PID_TYPES.get(endpoint)

    @staticmethod
    def _get_config_pid_types_to_endpoints():
        """Retrieve the map from pid_type to endpoint.

        Note:

            This function exists for the sake of testability
            otherwhise you have to bind all these util functions
            with the ``current_app``.
        """
        return current_app.config["PID_TYPES_TO_ENDPOINTS"]

    @staticmethod
    def _get_config_pid_types_to_schema():
        """Retrieve the map from pid_type to schema.

        Note:

            This function exists for the sake of testability
            otherwhise you have to bind all these util functions
            with the ``current_app``.
        """
        return current_app.config["PID_TYPES_TO_SCHEMA"]

    @staticmethod
    def get_pid_type_from_schema(schema):
        """Return the ``pid_type`` for a given ``schema``.

        Args:
            schema (str): the schema name.
                The schema name is the schema file name, for,
                example ``hep.json``  is the schema for ``hep``.
        Returns:
            None if not found, the ``pid_type``.
        """
        try:
            schema_name = (
                six.moves.urllib.parse.urlsplit(schema)
                .path.split("/")[-1]
                .split(".")[0]
            )
        except (TypeError, IndexError):
            schema_name = None
        pids_to_schema = PidStoreBase._get_config_pid_types_to_schema()
        return pids_to_schema.get(schema_name)

    @staticmethod
    def get_pid_from_record_uri(uri):
        parts = [part for part in uri.split("/") if part]
        try:
            pid_type = parts[-2][:3]
            pid_value = parts[-1]
        except IndexError:
            return None

        return pid_type, pid_value
