# -*- coding: utf-8 -*-

"""
  bloombox: schema
  ~~~~~~~~~~~~~~~~
  :copyright: (c) Momentum Ideas Co., 2018
  :license: This software makes use of the Apache License v2.
            A copy of this license is included as ``LICENSE.md`` in
            the root of the project.
"""

import sys, os


## calculate schema path and add to sys.path
schema_path = os.path.dirname(os.path.abspath(__file__))
if schema_path not in sys.path: sys.path.append(schema_path)

## preload some of the proto machinery
import grpc
from google import api
from google import protobuf

