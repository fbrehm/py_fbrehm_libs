#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Frank Brehm
@contact: frank@brehm-online.com
@copyright: (c) 2010-2011 by Frank Brehm, Berlin
@license: GPL3
@version: 0.0.1
@summary: This module includes the base logging object
'''

__author__ = 'Frank Brehm <frank@brehm-online.com>'
__copyright__ = '(C) 2010 by Frank Brehm, Berlin'
__contact__ = 'frank@brehm-online.com'
__version__ = '0.0.1'
__license__ = 'GPL3'

import logging

class LoggingObject(object):
    """Base object with a verbose level and a logging facility.
    """

    #------------------------------------------------------
    def __init__( self, verbose = 0, logger = None ):
        """Constructor.
        @param verbose: verbosity level (default: 0)
        @type verbose: int
        @param logger: a logger object for debugging a.s.o., will be created, if None
        @type logger: a logging.Logger object or None
        @return: None
        @rtype: None
        """

        if not isinstance( verbose, int ):
            raise Exception( "verbose is not an integer object" )

        self.verbose = verbose

        # Logging-Setup
        if logger is None:
            base_logger = self.init_base_logger()
            self.logger = self.init_logger(base_logger)
        elif isinstance( logger, logging.Logger ):
            self.logger = self.init_logger( logger )
        elif isinstance( logger, logging.LoggerAdapter ):
            self.logger = logger
            raise "self.logger is not a Logger or LoggerAdapter object"

    #------------------------------------------------------
    def init_logger( self, logger ):
        """Initializes a LoggerAdapter object and returns it.
        @param logger: a logger object for debugging a.s.o., will be created, if None
        @type logger: a logging.Logger object or None
        @return: None
        @rtype: None
        """

        new_logger = logging.LoggerAdapter( logger, { 'class_name': self.__class__.__name__ } )

        return new_logger

    #------------------------------------------------------
    def init_base_logger( self, logger_name = 'base_logger' ):
        """Initializes a logger object and returns it, maybe overwritten.
        @param logger_name: The name of the logging object
        @type logger_name: str
        @return: logger object
        @rtype: logging.Logger
        """

        # Logging-Setup
        loglevel = logging.WARNING
        logformat = '%(levelname)s: %(message)s'
        if self.verbose == 1:
            loglevel = logging.INFO
        elif self.verbose > 1:
            loglevel = logging.DEBUG
            logformat = '%(class_name)s - %(module)s.%(funcName)s(%(lineno)d) - %(levelname)s: %(message)s'

        base_logger = logging.getLogger(logger_name)
        base_logger.setLevel(loglevel)

        ch = logging.StreamHandler()
        ch.setLevel(loglevel)

        formatter = logging.Formatter(logformat)
        ch.setFormatter(formatter)

        base_logger.addHandler(ch)

        return base_logger

#-------------------------------------------------------------------------------------------------

# vim: fileencoding=utf-8 filetype=python ts=4 expandtab
