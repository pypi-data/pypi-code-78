# -*- coding:utf-8; tab-width:4; mode:python -*-

import logging
import functools
import inspect

from .path import child_relpath


class NullHandler(logging.Handler):
    def emit(self, record):
        pass


class CapitalLoggingFormatter(logging.Formatter):
    '''Define variable "levelcapital" for message formating. You can do things like:
    [EE] foo bar

    >>> formatter = CapitalLoggingFormatter('[%(levelcapital)s] %(message)s')
    >>> console = logging.StreamHandler()
    >>> console.setFormatter(formatter)
    '''
    def format(self, record):
        record.levelcapital = record.levelname[0] * 2
        return logging.Formatter.format(self, record)


class CallerData(object):
    """Get info about caller function, file, line and statement

    >>> def a():
    ...     return b()
    >>>
    >>> def b():
    ...     print CallerData()
    >>>
    >>> a()
    File "<stdin>", line 2, in a()
      return b()
    """
    def __init__(self, depth=0):
        frame = inspect.stack()[2 + depth]
        self.filename = child_relpath(inspect.getfile(frame[0]))
        self.line = inspect.getlineno(frame[0])
        self.funcname = frame[0].f_code.co_name
        try:
            self.statement = frame[4][0].strip()
        except TypeError:
            self.statement = None

    def __str__(self):
        return 'File "{0}", line {1}, in {2}()\n  {3}'.format(
            self.filename, self.line, self.funcname, self.statement)


class UniqueFilter(logging.Filter):
    """Log messages are allowed through just once.
    The 'message' includes substitutions, but is not formatted by the
    handler. If it were, then practically all messages would be unique!

    from: http://code.activestate.com/recipes/412552-using-the-logging-module/
    """
    def __init__(self, name=""):
        logging.Filter.__init__(self, name)
        self.reset()

    def reset(self):
        """Act as if nothing has happened."""
        self.__logged = {}

    def filter(self, rec):
        """logging.Filter.filter performs an extra filter on the name."""
        return logging.Filter.filter(self, rec) and self.__is_first_time(rec)

    def __is_first_time(self, rec):
        """Emit a message only once."""
        try:
            msg = rec.msg % (rec.args)
        except TypeError:
            msg = rec.msg

        if msg in self.__logged:
            self.__logged[msg] += 1
            return False
        else:
            self.__logged[msg] = 1
            return True


class PrefixLogger(logging.Logger):
    def __init__(self, logger, prefix):
        super(PrefixLogger, self).__init__(logger.name)
        self.logger = logger
        self.prefix = prefix

        for name in ['debug', 'info', 'warning', 'error', 'critical']:
            method = getattr(logger, name)
            setattr(self, name, functools.partial(self.log_prefix, method))

    def log_prefix(self, method, msg, *args):
        method(self.prefix + msg, *args)
