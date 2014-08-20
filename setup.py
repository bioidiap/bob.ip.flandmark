#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# Andre Anjos <andre.anjos@idiap.ch>
# Thu 20 Sep 2012 14:43:19 CEST

"""Bindings for flandmark
"""

bob_packages = ['bob.core', 'bob.io.base']

from setuptools import setup, find_packages, dist
dist.Distribution(dict(setup_requires=['bob.blitz'] + bob_packages))
from bob.blitz.extension import Extension

version = '2.0.0a0'

packages = ['boost', 'opencv>=2.0']
boost_modules = ['system']

setup(

    name="bob.ip.flandmark",
    version=version,
    description="Python bindings to the flandmark keypoint localization library",
    license="GPLv3",
    author='Andre Anjos',
    author_email='andre.anjos@idiap.ch',
    long_description=open('README.rst').read(),
    url='https://github.com/bioidiap/bob.ip.flandmark',

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'bob.blitz',
      'bob.core',
      'bob.io.base',
      'bob.io.image', #for tests
      'bob.ip.color', #for tests
      'bob.ip.draw', #for doc generation
      'matplotlib', #for doc generation
    ],

    namespace_packages=[
      "bob",
      "bob.ip",
    ],

    ext_modules=[
      Extension("bob.ip.flandmark.version",
        [
          "bob/ip/flandmark/version.cpp",
        ],
        bob_packages = bob_packages,
        version = version,
        packages = packages,
        boost_modules = boost_modules,
      ),

      Extension("bob.ip.flandmark._library",
        [
          "bob/ip/flandmark/flandmark_detector.cpp",
          "bob/ip/flandmark/liblbp.cpp",
          "bob/ip/flandmark/flandmark.cpp",
          "bob/ip/flandmark/main.cpp",
        ],
        bob_packages = bob_packages,
        version = version,
        packages = packages,
        boost_modules = boost_modules,
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
