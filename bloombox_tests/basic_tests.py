# -*- coding: utf-8 -*-

"""
  bloombox testsuite: basic tests
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  :copyright: (c) Momentum Ideas Co., 2018
  :license: This software makes use of the Apache License v2.
            A copy of this license is included as ``LICENSE.md`` in
            the root of the project.
"""

import unittest


class BasicLibraryTests(unittest.TestCase):

  """ Basic library tests. """

  def test_basic_import(self):

    """ Top-level: 'bloombox' should be importable. """

    import bloombox

  def test_toplevel_import(self):

    """ Top-level: 'bloombox.schema' and 'bloombox.client' should be importable. """

    from bloombox import schema
    from bloombox import client
