# -*- coding: utf-8 -*-

"""
  bloombox testsuite: schema tests
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  :copyright: (c) Momentum Ideas Co., 2018
  :license: This software makes use of the Apache License v2.
            A copy of this license is included as ``LICENSE.md`` in
            the root of the project.
"""

import unittest


class LibrarySchemaTests(unittest.TestCase):

  """ Schema object tests. """

  def test_schemas_import(self):

    """ Schemas: 'schema.base' objects should be importable. """

    from bloombox.schema.base import ProductKey_pb2
    from bloombox.schema.base import ProductKind_pb2
    from bloombox.schema.base import ProductType_pb2

  def test_products_import(self):

    """ Schemas: 'schema.products' objects should be importable. """

    from bloombox.schema.products import Flower_pb2
