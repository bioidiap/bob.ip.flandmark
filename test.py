#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 20 Sep 2012 17:21:36 CEST 

"""
"""

import sys
import bob
from _flandmark import Localizer

op = Localizer("flandmark/haarcascade_frontalface_alt.xml",
    "flandmark/flandmark_model.dat")

for f in bob.io.VideoReader('/scratch/aanjos/bob/python/bob/io/test/data/test.mov'):
  print "Hello!"
  print op(bob.ip.rgb_to_gray(f))
