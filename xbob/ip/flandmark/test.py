#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Wed 16 Apr 09:35:37 2014 CEST

"""Tests for flandmark python bindings
"""

import os
import pkg_resources
import nose.tools
import xbob.io
import xbob.ip.color

from . import Flandmark

def F(f):
  """Returns the test file on the "data" subdirectory"""
  return pkg_resources.resource_filename(__name__, os.path.join('data', f))

LENA = F('lena.jpg')
LENA_BBX = [
    (214, 202, 183, 183)
    ] #from OpenCV's cascade detector

MULTI = F('multi.jpg')
MULTI_BBX = [
    [326, 20, 31, 31],
    [163, 25, 34, 34],
    [253, 42, 28, 28],
    ] #from OpenCV's cascade detector

def opencv_detect(image):
  """Detects a face using OpenCV's cascade detector

  Returns a list of arrays containing (x, y, width, height) for each detected
  face.
  """

  from cv2 import CascadeClassifier, cv

  cc = CascadeClassifier(F('haarcascade_frontalface_alt.xml'))
  return cc.detectMultiScale(
      image,
      1.3, #scaleFactor (at each time the image is re-scaled)
      4, #minNeighbors (around candidate to be retained)
      0, #flags (normally, should be set to zero)
      (20,20), #(minSize, maxSize) (of detected objects)
      )

@nose.tools.nottest
def test_lena_opencv():

  img = xbob.io.load(LENA)
  gray = xbob.ip.color.rgb_to_gray(img)
  (x, y, width, height) = opencv_detect(gray)[0]

  flm = Flandmark()
  keypoints = flm.locate(gray, y, x, height, width)
  assert keypoints

def test_lena():

  img = xbob.io.load(LENA)
  gray = xbob.ip.color.rgb_to_gray(img)
  (x, y, width, height) = LENA_BBX[0]

  flm = Flandmark()
  keypoints = flm.locate(gray, y, x, height, width)
  assert keypoints
  nose.tools.eq_(len(keypoints), 8)

@nose.tools.nottest
def test_multi_opencv():

  img = xbob.io.load(MULTI)
  gray = xbob.ip.color.rgb_to_gray(img)
  bbx = opencv_detect(gray)

  flm = Flandmark()
  for (x, y, width, height) in bbx:
    keypoints = flm.locate(gray, y, x, height, width)
    assert keypoints

def test_multi():

  img = xbob.io.load(MULTI)
  gray = xbob.ip.color.rgb_to_gray(img)

  flm = Flandmark()
  for (x, y, width, height) in MULTI_BBX:
    keypoints = flm.locate(gray, y, x, height, width)
    assert keypoints
    nose.tools.eq_(len(keypoints), 8)
