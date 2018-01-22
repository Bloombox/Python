# -*- coding: utf-8 -*-

"""
  bloombox: setup
  ~~~~~~~~~~~~~~
  :copyright: (c) Momentum Ideas Co., 2018
  :license: This software makes use of the Apache License v2.
            A copy of this license is included as ``LICENSE.md`` in
            the root of the project.
"""

from setuptools import setup, find_packages


setup(
  name="bloombox",
  version="0.0.1",
  packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
  install_requires=['protobuf', 'grpcio'],
  author="Bloombox",
  author_email="info@bloombox.io",
  license="Apache 2.0",
  keywords="bloombox gRPC API client library",
  url="https://bloombox.io",
  project_urls={
    "Bug Tracker": "https://github.com/bloombox/python/issues",
    "Documentation": "https://bloombox.github.io/Python",
    "Source Code": "https://github.com/bloombox/python"
  })

