#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Fri 21 Sep 2012 10:43:12 CEST 

"""Annotates videos, dumps annotations as text files.
"""

import os
import sys
import bob
from .. import Localizer
import pkg_resources

def get_biggest(dets):
  """Returns the biggest detection found"""
  retval = dets[0]
  for d in dets[1:]:
    if retval['bbox'][2] < d['bbox'][2]: retval = d
  return retval

def main():

  import argparse

  parser = argparse.ArgumentParser(description=__doc__,
      formatter_class=argparse.RawDescriptionHelpFormatter)

  parser.add_argument('video', metavar='VIDEO', type=str,
      help="Video file to load")

  from ..version import __version__
  name = os.path.basename(os.path.splitext(sys.argv[0])[0])
  parser.add_argument('-V', '--version', action='version',
      version='Automatic Video Keypoint Annotation Tool v%s (%s)' % (__version__, name))

  args = parser.parse_args()

  if not os.path.exists(args.video):
    parser.error("Input video file '%s' cannot be read" % args.video)

  op = Localizer()
  v = bob.io.VideoReader(args.video)
  for k, frame in enumerate(v):
    dets = op(frame)
    if dets:
      biggest = get_biggest(dets)
      bbox = biggest['bbox']
      landmarks = biggest['landmark']
      print "%d %d %d %d %d" % ((k,) + bbox),
      for pair in landmarks:
        print "%d %d" % (round(pair[0]), round(pair[1])),
      print ""
    else:
      print "%d 0 0 0 0" % k
