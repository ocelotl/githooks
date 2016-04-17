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

from commit_message import check_commit_message


def test_action():
    """
    Test that the correct action is passed in the commit message.

    This test focuses in the ACTION part of the commit message.
    """
    # Testing the right actions:
    commit_message = 'chg: This is the commit message.'

    assert check_commit_message(commit_message)

    commit_message = 'fix: This is the commit message.'

    assert check_commit_message(commit_message)

    commit_message = 'new: This is the commit message.'

    assert check_commit_message(commit_message)

    # Testing a wrong action:
    commit_message = 'var: This is the commit message.'

    assert not check_commit_message(commit_message)

    # Testing a missing action:
    commit_message = 'This is the commit message.'

    assert not check_commit_message(commit_message)


def test_audience():
    """
    Test that the correct audience is passed in the commit message.

    This test focuses in the AUDIENCE part of the commit message.
    """
    # Testing the right audiences:
    commit_message = 'chg: dev: This is the commit message.'

    assert check_commit_message(commit_message)

    commit_message = 'chg: usr: This is the commit message.'

    assert check_commit_message(commit_message)

    commit_message = 'chg: pkg: This is the commit message.'

    assert check_commit_message(commit_message)

    commit_message = 'chg: test: This is the commit message.'

    assert check_commit_message(commit_message)

    commit_message = 'chg: doc: This is the commit message.'

    assert check_commit_message(commit_message)

    # Testing a wrong audience:
    commit_message = 'chg: var: This is the commit message.'

    assert not check_commit_message(commit_message)


def test_message():
    """
    Test that the correct message is passed in the commit message.

    This test focuses in the COMMIT_MSG part of the commit message.
    """
    # Testing the wrong messages:
    commit_message = 'chg: This is the commit message'

    assert not check_commit_message(commit_message)

    commit_message = 'chg: his is the commit message.'

    assert not check_commit_message(commit_message)

    commit_message = 'chg: This is the commit message. And'

    assert not check_commit_message(commit_message)

    commit_message = (
        'chg: This is the commit message but is way, way too '
        'long.'
    )

    assert not check_commit_message(commit_message)


def test_tag():
    """
    Test that the correct tag is passed in the commit message.

    This test focuses in the TAG part of the commit message.
    """
    # Testing the wrong messages:
    commit_message = 'chg: This is the commit message. !refactor'

    assert check_commit_message(commit_message)

    commit_message = 'chg: This is the commit message. !minor'

    assert check_commit_message(commit_message)

    commit_message = 'chg: This is the commit message. !cosmetic'

    assert check_commit_message(commit_message)

    commit_message = 'chg: This is the commit message. !wip'

    assert check_commit_message(commit_message)

    commit_message = 'chg: This is the commit message. !var'

    assert not check_commit_message(commit_message)


def test_rest():
    """
    Test that the correct rest of the message is passed in the commit message.

    This test focuses in the rest of the message part of the commit message.
    """
    # Testing the rest of the message messages:
    commit_message = (
        'chg: This is the commit message. !refactor\n\nSomething'
    )

    assert check_commit_message(commit_message)

    commit_message = (
        'chg: This is the commit message. !refactor\n\nSomething\nSomething'
    )

    assert check_commit_message(commit_message)

    # Testing the wrong rest of the message messages:
    commit_message = (
        'chg: This is the commit message. !refactor\n'
    )

    assert not check_commit_message(commit_message)
