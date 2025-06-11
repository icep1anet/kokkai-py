# Author: iceplanet <X@icep1anet>
# Copyright (c) 2025 iceplanet
# License: MIT

from setuptools import setup
import kokkai_py

DESCRIPTION = "seaborn-analyzer: data visualization of regression, classification and distribution"
NAME = 'kokkai-py'
AUTHOR = 'icep1anet'
AUTHOR_EMAIL = 'X@icep1anet'
URL = 'https://github.com/icep1anet/kokkai-py'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/icep1anet/kokkai-py'
VERSION = kokkai_py.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
]

PACKAGES = [
    'kokkai-py'
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Topic :: Scientific/Engineering',
]

with open('README.rst', 'r') as fp:
    readme = fp.read()
with open('CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      keywords='kokkai, parliament, japan',
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
    )
