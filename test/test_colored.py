#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: (c) 2010-2012 Frank Brehm, Berlin
@license: LGPLv3+
@summary: unittest for colored console logging formatter
"""



import unittest
import os
import sys

libdir = os.path.abspath(os.path.join(
        os.path.dirname(sys.argv[0]), '..', 'src'))
sys.path.insert(0, libdir)

import fbrehm.logging.colored

from fbrehm.logging.colored import COLOR_CODE
from fbrehm.logging.colored import colorstr
from fbrehm.logging.colored import ColoredFormatter


class TestColoredFormatter(unittest.TestCase):

    def setUp(self):
        pass

    def test_colorcode(self):

        msg = "Colored output"

        for key in sorted(COLOR_CODE.keys()):

            try:
                print '%s: %s' % (key, colorstr(msg, key))
            except Exception, e:
                self.fail("Failed to generate colored string %r with %s: %s" % (
                        key, e.__class__.__name__, str(e)))

    def test_object(self):

        try:
            formatter = ColoredFormatter(
                    '%(name)s: %(message)s (%(filename)s:%(lineno)d)')
        except Exception, e:
            self.fail("Could not instatiate ColoredFormatter object with %s: %s" % (
                    e.__class__.__name__, str(e)))

#==============================================================================

if __name__ == '__main__':

    import argparse

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("-v", "--verbose", action = "count",
            dest = 'verbose', help = 'Increase the verbosity level')
    args = arg_parser.parse_args()

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromName(
            'test_colored.TestColoredFormatter.test_colorcode'))
    suite.addTests(loader.loadTestsFromName(
            'test_colored.TestColoredFormatter.test_object'))

    runner = unittest.TextTestRunner(verbosity = args.verbose)

    result = runner.run(suite)

#==============================================================================

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4 nu
