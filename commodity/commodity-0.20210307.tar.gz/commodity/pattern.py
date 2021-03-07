# -*- coding:utf-8; tab-width:4; mode:python -*-
"""
.. module:: pattern
   :synopsis: Common pythonic design pattern

.. moduleauthor:: David Villa Alises <David.Villa@gmail.com>
"""

import collections
import string
import inspect
from functools import partial

# Borg pattern

from .type_ import checked_type

try:
    unicode
except NameError:
    unicode = str


    # Exceptions
#    class ObserverException(Exception):
#        def __str__(self):
#            return "%s: %s" % (self.__class__.__name__, Exception.__str__(self))


def make_exception(name, message=''):
    return type(name, (Exception,), {})


class DummyLogger(object):
    def debug(self, *args):
        pass

    def warning(self, *args):
        pass


# other: http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/

def memoized(method_or_arg_spec=None, ignore=None):
    """Memoized decorator for functions and methods, including classmethods, staticmethods and
    properties

    >>> import random
    >>>
    >>> @memoized
    ... def get_identifier(obj):
    ...     return random.randrange(1000)
    ...
    >>> n1 = get_identifier("hi")
    >>> n2 = get_identifier("hi")
    >>> assert n1 == n2

    It allows to ignore some arguments in memoization, so different values for those
    arguments DO NOT implies new true invocations:

    >>> @memoized(ignore=['b'])
    ... def gen_number(a, b):
    ...     return random.randrange(1000)
    ...
    >>> n1 = gen_number(1, 2)
    >>> n2 = gen_number(1, 3)
    >>> print n1, n2
    >>> assert n1 == n2

    * http://pko.ch/2008/08/22/memoization-in-python-easier-than-what-it-should-be/
    * http://micheles.googlecode.com/hg/decorator/documentation.html

    """
    if method_or_arg_spec is not None:
        return _memoized(func=method_or_arg_spec)

    return partial(_memoized, ignore=ignore)


class _memoized(object):
    def __init__(self, func, ignore=None):
        self.instance = None
        self.func = func
        self.cache = {}

        self.ignore = checked_type(list, ignore or [])

        self.argspec = inspect.getargspec(func).args

    def hash_args(self, *args, **kargs):
        args = self.filterout_ignored(args)
        if kargs:
            return args, frozenset(kargs.iteritems())

        return args

    def pack_args(self, args):
        if self.instance is None:
            return args

        return (self.instance,) + args

    def __get__(self, instance, owner):
        self.instance = instance
        return self

    def filterout_ignored(self, args):
        args = list(args)
        for n in self.ignore:
            try:
                pos = self.argspec.index(n)
                del args[pos]
            except ValueError:
                raise ValueError("%s() has not argument '%s'" % (self.func.__name__, n))

        return tuple(args)

    def __call__(self, *args, **kargs):
        cache_args = self.pack_args(args)

        key = self.hash_args(*cache_args, **kargs)

        if key not in self.cache:
            self.cache[key] = self.func(*cache_args, **kargs)

        return self.cache[key]

    def repr(self):
        return "memoized({0})".format(self.func)


# EXPERIMENTAL, DO NOT USE IN PRODUCTION CODE
# from cached_property in http://wiki.python.org/moin/PythonDecoratorLibrary
# replace this with:
#
#   @property
#   @lru_cache  # from collections import lru_cache
#   def method(self):
#
class memoizedproperty(object):
    """Memoized properties

    >>> import random
    >>> class A:
    ...     @memoizedproperty
    ...     def a_property(self):
    ...         return random.randrange(1000)
    ...
    >>> a1 = A()
    >>> v1 = a1.a_property
    >>> v2 = a1.a_property
    >>> assert v1 == v2
    """

    def __init__(self, method):
        self.method = method
        self.instance = None
        self.cache = {}

    def __get__(self, instance, owner):
        self.instance = instance
        if instance not in self.cache:
            self.cache[instance] = self.method(instance)

        return self.cache[instance]

    def reset(self):
        del self.cache[self.instance]


class Flyweight(type):
    '''Flyweight dessign pattern (for identical objects) as metaclass

    python-2:
    >>> class Sample(object):
    ...     __metaclass__ = Flyweight

    python-3:
    >>> class Sample(metaclass=Flyweight):
            pass
    '''

    def __init__(cls, name, bases, dct):
        cls.__instances = {}
        type.__init__(cls, name, bases, dct)

    def __call__(cls, key, *args, **kw):
        instance = cls.__instances.get(key)
        if instance is None:
            instance = type.__call__(cls, key, *args, **kw)
            cls.__instances[key] = instance
        return instance


class Observable(object):
    InvalidObserver = make_exception('InvalidObserver', 'observer must be callable')
    NotSuchObserver = make_exception('NotSuchObserver')
    ObserverException = make_exception('ObserverExcepton')

    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if not callable(observer):
            raise self.InvalidObserver()

        if observer in self.observers:
            return

        self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            raise self.NotSuchObserver(observer)

    def notify(self, value):
        for observer in self.observers:
            try:
                observer(value)
            except Exception as ex:
                raise self.ObserverException(ex)


# http://books.google.es/books?id=9_AXCmGDiz8C&lpg=PA9&pg=PA34&redir_esc=y#v=onepage&q&f=false
class Bunch(dict):
    """It provides dict keys as attributes and viceversa

    >>> data = dict(ccc=2)
    >>> bunch = Bunch(data)
    >>> bunch.ccc
    2
    >>> bunch.ddd = 3
    >>> bunch['ddd']
    3
    >>> bunch['eee'] = 4
    >>> bunch.eee
    4
    """
    def __init__(self, *args, **kargs):
        super(Bunch, self).__init__(*args, **kargs)
        self.__dict__ = self

    def copy(self):
        return self.__class__(**self)

    def __repr__(self):
        items = []
        for key in self.keys():
            items.append("'%s': %s" % (key, repr(getattr(self, key))))

        return "Bunch({0})".format(str.join(', ', items))


class NestedBunch(Bunch):
    """Bunch with recursive fallback in other bunch (its parent)

    >>> a = NestedBunch()
    >>> a.foo = 1
    >>> a2 = a.new_layer()
    >>> a2.bar = 2
    >>> a2.foo
    1
    >>> a2.keys()
    ['foo', 'bar']

    >>> b = NestedBunch()
    >>> b.foo = 1
    >>> b2 = b.new_layer()
    >>> b2.foo
    1
    >>> b2['foo'] = 5000
    >>> b2.foo
    5000
    >>> b['foo']
    1

    >>> c = NestedBunch()
    >>> c.foo = 1
    >>> c2 = c.new_layer().new_layer()
    >>> c2.foo
    1
    """
    def __init__(self, *args, **kargs):
        super(NestedBunch, self).__init__(*args, **kargs)
        self.__parent = None

    def new_layer(self):
        retval = NestedBunch()
        retval.__parent = self
        return retval

    def __getitem__(self, key):
        try:
            return getattr(self, key)
        except AttributeError:
            if self.__parent is None:
                raise KeyError

            return getattr(self.__parent, key)

    def __getattr__(self, key):
        if self.__parent is None:
            raise AttributeError

        return self.__parent[key]

    def __dict_method(self, method):
        retval = []
        if self.__parent:
            retval.extend(getattr(self.__parent, method)())

        retval.extend(getattr(super(NestedBunch, self), method)())
        return retval

    def keys(self):
        retval = self.__dict_method('keys')
        retval.remove('_NestedBunch__parent')
        return retval

    def items(self):
        retval = self.__dict_method('items')
        retval.remove(('_NestedBunch__parent', self.__parent))
        return retval

    def values(self):
        retval = self.__dict_method('values')
        retval.remove(self.__parent)
        return retval


class MetaBunch(collections.MutableMapping):
    '''
    A bunch of bunches. It allows to recursively access keys as
    attributes and viceversa.  It may decorate any mapping type.

    >>> b = MetaBunch()
    >>> b['aaa'] = {'bbb': 1}
    >>> b.aaa.bbb
    1
    >>> b.aaa.ccc = 2
    >>> b['aaa']['ccc']
    2

    '''

    def __init__(self, dct=None):
        if dct is None:
            dct = dict()

        self.__dict__['dct'] = checked_type(collections.Mapping, dct)

    def __iter__(self):
        return iter(self.dct)

    def __len__(self):
        return len(self.dct)

    def __repr__(self):
        return repr(self.dct)

    def __getitem__(self, key):
        retval = self.dct

        for key in self.keypath(key):
            checked_type(collections.Mapping, retval)
            retval = retval[key]

        if isinstance(retval, collections.Mapping) and \
                not isinstance(retval, MetaBunch):
            return MetaBunch(retval)

        return retval

    def __setitem__(self, key, value):
        dct = self.dct
        keys = self.keypath(key)

        for key in keys[:-1]:
            if key not in dct:
                dct[key] = {}

            dct = dct[key]

        dct[keys[-1]] = value

    def __delitem__(self, key):
        dct = self.dct
        keys = self.keypath(key)

        for key in keys[:-1]:
            dct = dct[key]

        del dct[keys[-1]]

    def keypath(self, key):
        checked_type(str, key)
        return key.split('.')

    def __contains__(self, key):
        return self._private_has_key(key)

    def has_key(self, key):
        return self._private_has_key(key)

    def _private_has_key(self, key):
        dct = self.dct

        try:
            for key in self.keypath(key):
                dct = dct[key]
        except (KeyError, TypeError):
            return False

        return True

    def __getattr__(self, attr):
        try:
            retval = self.__dict__['dct'][attr]
        except KeyError:
            raise AttributeError(attr)

        if isinstance(retval, collections.Mapping) and \
                not isinstance(retval, MetaBunch):
            return MetaBunch(retval)

        return retval

    def __setattr__(self, attr, value):
        self[attr] = value


class TemplateBunch(collections.MutableMapping):
    """A Bunch automatically templated with its own content

    >>> t = TemplateBunch()
    >>> t.name = "Bob"
    >>> t.greeting = "Hi $name!"
    >>> t.greeting
    "Hi Bob!"
    >>> t.person = "$name's sister"
    >>> t.greeting = "Hi $person!"
    >>> t.person
    "Bob's sister"
    >>> t.greeting
    "Hi Bob's sister"
    """
    def __init__(self):
        self.__dict__['dct'] = Bunch()

    def __iter__(self):
        return iter(self.dct)

    def __len__(self):
        return len(self.dct)

    def __repr__(self):
        return repr(self.dct)

    def __delitem__(self, key):
        del self.dct[key]

    def has_key(self, key):
        return key in self.dct

    def __setattr__(self, attr, value):
        self.dct[attr] = value

    def __getattr__(self, attr):
        try:
            value = self.dct[attr]
        except KeyError:
            raise AttributeError(attr)

        if isinstance(value, (str, unicode)):
            return string.Template(value).safe_substitute(self)

        return value

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __getitem__(self, key):
        try:
            return self.__getattr__(key)
        except AttributeError:
            raise KeyError(key)

    def clear(self):
        self.dct.clear()
