#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 20 Sep 2012 14:43:19 CEST

"""Bindings for flandmark
"""

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['xbob.blitz', 'xbob.io']))
from xbob.blitz.extension import Extension
import xbob.io

version = '2.0.0a0'
packages = ['opencv>=2.0']

include_dirs = [xbob.io.get_include()]

setup(

    name="xbob.ip.flandmark",
    version=version,
    description="Python bindings to the flandmark keypoint localization library",
    license="GPLv3",
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',
    long_description=open('README.rst').read(),
    url='https://github.com/bioidiap/xbob.ip.flandmark',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'xbob.blitz',
      'xbob.io', #for tests
    ],

    namespace_packages=[
      "xbob",
      "xbob.ip",
      ],

    entry_points = {
      'console_scripts': [
        'xbob_flandmark.py = xbob.flandmark.script.annotate:main',
        ],
      },

    ext_modules=[
      Extension("xbob.ip.flandmark.version",
        [
          "xbob/ip/flandmark/version.cpp",
          ],
        version = version,
        packages = packages,
        ),
      Extension("xbob.ip.flandmark._library",
        [
          "xbob/ip/flandmark/flandmark_detector.cpp",
          "xbob/ip/flandmark/liblbp.cpp",
          "xbob/ip/flandmark/flandmark.cpp",
          "xbob/ip/flandmark/main.cpp",
          ],
        version = version,
        packages = packages,
        ),
      ],

    classifiers = [
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      ],

    )
