#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Wed 16 Apr 09:35:37 2014 CEST

"""Tests for flandmark python bindings
"""

import os
import bob
import pkg_resources
import nose.tools

from . import Localizer

def F(name, f):
  """Returns the test file on the "data" subdirectory"""
  return pkg_resources.resource_filename(name, os.path.join('data', f))

INPUT_VIDEO = F('xbob.io', 'test.mov')

def test_video():

  op = Localizer()

  for f in bob.io.VideoReader(INPUT_VIDEO):
    assert op(f)
