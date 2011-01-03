#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: (c) 2010-2011 by Frank Brehm, Berlin
@license: GPL3
@version: 0.0.2
@summary: This module handle all getopt stuff
'''

__author__ = 'Frank Brehm <frank@brehm-online.com>'
__copyright__ = '(C) 2010 by Frank Brehm, Berlin'
__version__ = '0.0.2'

import os
import sys

from optparse import OptionError
from optparse import OptionParser
from optparse import OptionConflictError

class BaseOptParser(object):
    '''
    This is the base class for Option Parsing. All other getopts classes should
    derived from this class. This class adds the default cmd named options like
    '--test' and '--verbose'.
    It implements also all callback functions/methods - so no class has to
    write its own callback and every callback is reusable for every class.
    @author: Robin Wittler / Frank Brehm
    @contact: robin.wittler@profitbricks.com / frank@brehm-online.com
    '''

    #---------------------------------------------------------------------
    def __init__( self, prog = '%prog',
                        version = None,
                        description = '',
                        usage = 'Usage: %s [options]',
                        test_option = False
    ):
        '''
        Costructor.
        @param prog: The name of the calling process (e.g. sys.argv[0])
        @type prog: str
        @param version: The version string to use
        @type version: str
        @param description: The Description the process should use
        @type description: str
        @param usage: An usage string fro the help screen, must have a '%s' for the program name
        @type usage: str
        @param test_option: should a test/simulate option be created? - default False
        @type test_option: boolean
        @return: None
        '''

        self.prog = prog
        self.version = version
        self.description = description
        self.usage = usage %(prog)

        self.options = None
        self.args = None
        self.__options_set = False
        self.__action_set = None
        self.parsed = False

        self.parser = OptionParser(
                prog        = self.prog,
                version     = self.version,
                description = self.description,
                usage       = self.usage
        )

        if test_option:
            self.addOption(
                    '--simulate',
                    '--test',
                    '-T',
                    default = False,
                    action  = 'store_true',
                    dest    = 'test',
                    help    = 'set this do simulate commands'
            )

        self.addOption(
                '--verbose',
                '-v',
                default = False,
                action  = 'count',
                dest    = 'verbose',
                help    = 'set the verbosity level'
        )

    #----------------------------------------------------------------------
    def getOpts(self):
        '''
        The baseimplentation of getOpts. It ensures that evry class
        which derived from the base class have to call the 'addOption'
        method first to add some options.
        @return: None
        '''
        if not self.__options_set:
            raise RuntimeError(
                    'You must call addOption first.'
            )
        if not self.parsed:
            self.options, self.args = self.parser.parse_args()
            self.parsed = True

    #----------------------------------------------------------------------
    def addOption(self, *targs, **kwargs):
        '''
        This Method adds the options to the parser instance.
        @param targs: The getopts cmd param names (e.g. '--help', '-h')
        @type targs: tuple
        @param kwargs: The named getopts options (e.g. 'dest', 'help',
        'callback')
        @type kwargs: dict
        @return: None
        @rtype: None
        '''
        self.parser.add_option(*targs, **kwargs)
        if not self.__options_set:
            self.__options_set = True

    #----------------------------------------------------------------------
    def setBaseOptionHelp( self, option_name, option_help ):
        '''This method sets the help text of the named option.
        @param option_name: The name of the option to change
        @type option_name: str
        @param option_help: The new option help text
        @type option_help: str
        @return: None
        @rtype: None
        '''

        if not len(option_name):
            raise SyntaxError( "empty option name given." )

        as_long_option = True
        if len(option_name) == 1: as_long_option = False

        for option in self.parser.option_list:
            opt_found = False
            if as_long_option:
                o = '--' + option_name
                for opt in option._long_opts:
                    if o == opt:
                        opt_found = True
                        break
            else:
                o = '-' + option_name
                for opt in option._short_opts:
                    if o == opt:
                        opt_found = True
                        break
            if opt_found:
                option.help = option_help
                break

    #---------------------------------------------------------------------



# vim: fileencoding=utf-8 filetype=python ts=4 expandtab
