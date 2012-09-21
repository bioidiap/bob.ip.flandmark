#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 20 Sep 2012 14:43:19 CEST 

"""Bindings for flandmark
"""

import sys
import subprocess
from distutils.core import setup
from distutils.extension import Extension

def pkgconfig(package):

  def uniq(seq, idfun=None):
    # order preserving
    if idfun is None:
      def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
      marker = idfun(item)
      # in old Python versions:
      # if seen.has_key(marker)
      # but in new ones:
      if marker in seen: continue
      seen[marker] = 1
      result.append(item)
    return result

  flag_map = {
      '-I': 'include_dirs',
      '-L': 'library_dirs',
      '-l': 'libraries',
      }

  cmd = [
      'pkg-config',
      '--libs',
      '--cflags',
      package,
      ]

  proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
      stderr=subprocess.STDOUT)

  output = proc.communicate()[0]

  if proc.returncode != 0:
    raise RuntimeError, "PkgConfig did not find package %s. Output:\n%s" % \
        (package, output.strip())

  kw = {}

  for token in output.split():
    if flag_map.has_key(token[:2]):
      kw.setdefault(flag_map.get(token[:2]), []).append(token[2:])

    else: # throw others to extra_link_args
      kw.setdefault('extra_compile_args', []).append(token)

  for k, v in kw.iteritems(): # remove duplicated
    kw[k] = uniq(v)

  return kw

def setup_bob_extension(ext_name, sources):
  """Sets up a given C++ extension that depends on Bob"""

  bob = pkgconfig('bob-python')
  ocv = pkgconfig('opencv')

  return Extension(
      ext_name,
      sources=sources,
      language="c++",
      include_dirs=bob['include_dirs'] + ocv['include_dirs'],
      library_dirs=bob['library_dirs'] + ocv.get('library_dirs', []),
      runtime_library_dirs=bob['library_dirs'] + ocv.get('library_dirs', []),
      libraries=bob['libraries'] + ocv['libraries'],
      )

setup(
    name="flandmark",
    version="1.0.6",
    ext_modules=[
      setup_bob_extension("flandmark._flandmark",
        [
          "flandmark/ext/flandmark_detector.cpp",
          "flandmark/ext/liblbp.cpp",
          "flandmark/ext/ext.cpp",
        ])
      ])
