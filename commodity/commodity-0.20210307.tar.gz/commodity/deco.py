# -*- coding:utf-8; tab-width:4; mode:python -*-

import functools
import logging


def tag(name):
    """Add boolean attributes to functions:

    >>> @tag('hidden')
    ... def func(args):
    ...     pass
    ...
    >>> func.hidden
    True
    """

    def wrap(f):
        setattr(f, name, True)
        return f
    return wrap


def add_attr(name, value):
    """Set the given function attribute:

    >>> @add_attr('timeout', 4)
    ... def func(args):
    ...     pass
    ...
    >>> func.timeout
    4
    """

    def wrap(f):
        setattr(f, name, value)
        return f
    return wrap


def handle_exception(exception, handler):
    """Add and exception handler with decorator

    >>> import logging, math
    >>> @handle_exception(ValueError, logging.error)
    ... def silent_sqrt(value):
    ...     return math.sqrt(value)
    >>> silent_sqrt(-1)
    ERROR:root:math domain error
    """

    def wrap(func):
        def wrapped(*args, **kargs):
            try:
                return func(*args, **kargs)
            except exception as e:
                handler(e)

        return wrapped
    return wrap


def suppress_errors(func=None, default=None, log_func=logging.debug, errors=[Exception]):
    """Decorator that avoids to create try/excepts only to avoid valid errors.
    It can return a default value and ignore only some exceptions.

    Example: It will return the file content or the empty string if it doesn't exists:

    >>> @suppress_errors(errors=[IOError], default='')
    ... def read_file(filename):
    ...     with file(filename) as f:
    ...         return f.read()

    >>> read_file('/some/not/exists')
    ''

    :param func: Function to be called.
    :param default: Default value to be returned if any of the exceptions are launched.
    :param log_func: The log function. logging.debug by default. It is a good idea to use it to avoid 'catch pokemon' problems.
    :param errors: list of allowed Exceptions. It takes in mind inheritance.
    """
    def decorator(func, *myargs):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                for error in errors:
                    if isinstance(e, error):
                        log_func(e)
                        return default
                raise

        wrap = wrapper

        # Try to look like the wrapped method.
        # update_wrapper fails with unnamed functions.
        if hasattr(func, '__name__'):
            functools.update_wrapper(wrap, func)

        return wrap

    if func is None:
        return decorator

    return decorator(func)
