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
This module implements a commit message checker.

The purpose of this is to check that a certain commit message is compliant with
a certain standard (defined in http://chris.beams.io/posts/git-commit/) to make
commit message checking fast.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from re import match, MULTILINE


def check_commit_message(commit_message):
    """
    Check that commit message is compliant.

    :param str commit_message: The commit message to check for correctness
    :rtype: bool
    :return: True if the commit message is compliant, False otherwise.
    """
    # The commit message format is checked to verify that is complian with
    # gitchangelog:
    # https://github.com/vaab/gitchangelog/blob/master/gitchangelog.rc.reference

    # r'(chg|fix|new): ((dev|usr|pkg|test|doc):)? [A-Z].{0,43}(?!\.) (!('
    # 'refactor|minor|cosmetic|wip))(\n(\n.{0,72})*)?', commit_message
    message_match = match(
        r'(chg|fix|new):( (dev|usr|pkg|test|doc):)? [A-Z].{0,48}?\.'
        r'( !(refactor|minor|cosmetic|wip))?$(\n(\n.{0,72})+)?(?!\n)',
        commit_message,
        MULTILINE
    )

    if message_match:
        return True

    return False


__all__ = ['check_commit_message']
