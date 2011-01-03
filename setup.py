#!/usr/bin/env python

# $Id$
# $URL$

from distutils.core import setup

long_description = '''
This is a collection of common usable python modules
made by Frank Brehm.
'''

setup( name = 'fbrehm-libs',
       version = '0.2',
       description = 'collection of common python modules by Frank Brehm',
       long_description = long_description,
       author = 'Frank Brehm',
       author_email = 'frank@brehm-online.com',
       url = 'http://www.brehm-online.com/projects/fbrehm-libs',
       packages = [ 'fbrehm', 'fbrehm.common', ],
       package_dir = {'': 'src'},
       license = 'GPL-3',
)

