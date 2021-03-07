# -*- coding:utf-8; tab-width:4; mode:python -*-

import inspect


def checked_type(cls, val):
    '''If 'val' is a instance of 'cls' returns 'val'. Otherwise raise TypeError.

    >>> checked_type(int, 3)
    3
    >>> checked_type((str, int), '4')
    '4'
    >>> checked_type(str, 5)
    TypeError: str is required, not int: '5'.
    '''
    if isinstance(val, cls):
        return val

    if isinstance(cls, tuple):
        expected = str.join(', ', [x.__name__ for x in cls])
    else:
        expected = cls.__name__

    raise TypeError("{0} is required, not {1}: '{2}'.".format(
        expected, val.__class__.__name__, val))


def module_to_dict(module):
    '''Return module global vars as a dict'''

    return dict([(k, v) for k, v in module.__dict__.items()
                 if not k.startswith('__') and not inspect.ismodule(v)])
