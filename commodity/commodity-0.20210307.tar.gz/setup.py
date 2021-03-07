#!/usr/bin/env python

# Copyright (C) 2012, 2015 David Villa Alises
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os
import sys
from setuptools import setup, find_packages


def local_open(fname):
    return open(os.path.join(os.path.dirname(__file__), fname))


exec(open('version.py').read())


config = dict(
    name         = 'commodity',
    version      = __version__,
    description  = 'General purpose python utilities library',
    author       = 'David Villa Alises',
    author_email = 'David.Villa@gmail.com',
    url          = 'https://bitbucket.org/arco_group/python-commodity',
    license      = 'GPLv3',
    packages     = find_packages(),
    provides     = ['commodity'],
    classifiers      = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)


if sys.version_info >= (3,):
    config.update(dict(
        use_2to3=True,
    ))

setup(**config)
