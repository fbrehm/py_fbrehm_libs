#!/usr/bin/env python

import os
import sys
from distutils.core import setup

# own modules:
cur_dir = os.getcwd()
if sys.argv[0] != '' and sys.argv[0] != '-c':
    cur_dir = os.path.dirname(sys.argv[0])
if os.path.exists(os.path.join(cur_dir, 'src', 'fbrehm')):
    sys.path.insert(0, os.path.abspath(os.path.join(cur_dir, 'src')))
del cur_dir

import fbrehm

packet_version = fbrehm.__version__

long_description = '''
This is a collection of common usable python modules
made by Frank Brehm.
'''

setup( name = 'fbrehm',
    version = packet_version,
    description = 'collection of common python modules by Frank Brehm',
    long_description = long_description,
    author = 'Frank Brehm',
    author_email = 'frank@brehm-online.com',
    url = 'http://www.brehm-online.com/projects/fbrehm-libs',
    license = 'LGPLv3+',
    platforms = ['posix'],
    packages = [
        'fbrehm',
        'fbrehm.common',
        'fbrehm.logging',
    ],
    package_dir = {'': 'src'},
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    provides = [
        'fbrehm',
    ],
    requires = [
        'argparse',
        'configobj',
    ]
)

#========================================================================

# vim: fileencoding=utf-8 filetype=python ts=4 expandtab
