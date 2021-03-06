#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2020  CZ.NIC, z. s. p. o.
#
# This file is part of FRED.
#
# FRED is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FRED is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FRED.  If not, see <https://www.gnu.org/licenses/>.
from __future__ import unicode_literals

__all__ = ["DummyLogger"]


class DummyLogger(object):
    """Dummy Logger. Never logs anything and never fails.

    Used to imitate normal logger, when you don't want to log anything (e.g.
    because you don't want to connect via Corba).
    """

    request_type_codes = {}
    result_codes = {}
    object_types = {}
    default_results = {}

    def __init__(self, *args, **kwargs):
        pass

    def start_session(self, *args, **kwargs):
        pass

    def create_request(self, *args, **kwargs):
        return DummyLogRequest()

    def create_dummy_request(self, *args, **kwargs):
        return DummyLogRequest()

    def close_session(self, *args, **kwargs):
        pass


class DummyLogRequest(object):
    def __init__(self, *args, **kwargs):
        self.request_id = 0
        self.service = ''
        self.request_type = ''
        self.result = ''

    def close(self, *args, **kwargs):
        pass
