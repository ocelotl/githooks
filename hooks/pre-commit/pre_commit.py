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
This module implements a pre commit test runner.

The purpose of this hook is to run the tests before the commit is applied so
that the history of the project so is guaranteed that any commit in the project
can be checked out yielding always a state where the tests pass.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from tox import cmdline


def run_tests():
    """
    Run tox to execute the tests.

    :rtype: bool
    :return: True if tox runs all tests successfully, False otherwise.
    """
    error = cmdline()

    if error == 0:
        return True

    return False


__all__ = ('run_tests')
