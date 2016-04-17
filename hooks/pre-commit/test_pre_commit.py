# -*- coding: UTF-8 -*-
#
# Copyright 2016 Diego "Ocelotl" Hurtado Pimentel
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module implements tests for the commit message checker.

This tests make sure that the commit message checker checks the right points in
the commit message.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from pre_commit import run_tests


@patch('pre_commit.cmdline')
def test_run_tests(mock_cmdline):
    """Test that the correct value is returned by run_tests."""
    mock_attrs = {'return_value': 0}

    mock_cmdline.configure_mock(**mock_attrs)

    assert run_tests()

    mock_attrs = {'return_value': 1}

    mock_cmdline.configure_mock(**mock_attrs)

    assert not run_tests()
