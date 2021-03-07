# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _analyserequation
else:
    import _analyserequation

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


SHARED_PTR_DISOWN = _analyserequation.SHARED_PTR_DISOWN
class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _analyserequation.delete_SwigPyIterator

    def value(self):
        return _analyserequation.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _analyserequation.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _analyserequation.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _analyserequation.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _analyserequation.SwigPyIterator_equal(self, x)

    def copy(self):
        return _analyserequation.SwigPyIterator_copy(self)

    def next(self):
        return _analyserequation.SwigPyIterator_next(self)

    def __next__(self):
        return _analyserequation.SwigPyIterator___next__(self)

    def previous(self):
        return _analyserequation.SwigPyIterator_previous(self)

    def advance(self, n):
        return _analyserequation.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _analyserequation.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _analyserequation.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _analyserequation.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _analyserequation.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _analyserequation.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _analyserequation.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _analyserequation:
_analyserequation.SwigPyIterator_swigregister(SwigPyIterator)

import libcellml.types
class AnalyserEquationVector(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _analyserequation.AnalyserEquationVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _analyserequation.AnalyserEquationVector___nonzero__(self)

    def __bool__(self):
        return _analyserequation.AnalyserEquationVector___bool__(self)

    def __len__(self):
        return _analyserequation.AnalyserEquationVector___len__(self)

    def __getslice__(self, i, j):
        return _analyserequation.AnalyserEquationVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _analyserequation.AnalyserEquationVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _analyserequation.AnalyserEquationVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _analyserequation.AnalyserEquationVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _analyserequation.AnalyserEquationVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _analyserequation.AnalyserEquationVector___setitem__(self, *args)

    def pop(self):
        return _analyserequation.AnalyserEquationVector_pop(self)

    def append(self, x):
        return _analyserequation.AnalyserEquationVector_append(self, x)

    def empty(self):
        return _analyserequation.AnalyserEquationVector_empty(self)

    def size(self):
        return _analyserequation.AnalyserEquationVector_size(self)

    def swap(self, v):
        return _analyserequation.AnalyserEquationVector_swap(self, v)

    def begin(self):
        return _analyserequation.AnalyserEquationVector_begin(self)

    def end(self):
        return _analyserequation.AnalyserEquationVector_end(self)

    def rbegin(self):
        return _analyserequation.AnalyserEquationVector_rbegin(self)

    def rend(self):
        return _analyserequation.AnalyserEquationVector_rend(self)

    def clear(self):
        return _analyserequation.AnalyserEquationVector_clear(self)

    def get_allocator(self):
        return _analyserequation.AnalyserEquationVector_get_allocator(self)

    def pop_back(self):
        return _analyserequation.AnalyserEquationVector_pop_back(self)

    def erase(self, *args):
        return _analyserequation.AnalyserEquationVector_erase(self, *args)

    def __init__(self, *args):
        _analyserequation.AnalyserEquationVector_swiginit(self, _analyserequation.new_AnalyserEquationVector(*args))

    def push_back(self, x):
        return _analyserequation.AnalyserEquationVector_push_back(self, x)

    def front(self):
        return _analyserequation.AnalyserEquationVector_front(self)

    def back(self):
        return _analyserequation.AnalyserEquationVector_back(self)

    def assign(self, n, x):
        return _analyserequation.AnalyserEquationVector_assign(self, n, x)

    def resize(self, *args):
        return _analyserequation.AnalyserEquationVector_resize(self, *args)

    def insert(self, *args):
        return _analyserequation.AnalyserEquationVector_insert(self, *args)

    def reserve(self, n):
        return _analyserequation.AnalyserEquationVector_reserve(self, n)

    def capacity(self):
        return _analyserequation.AnalyserEquationVector_capacity(self)
    __swig_destroy__ = _analyserequation.delete_AnalyserEquationVector

# Register AnalyserEquationVector in _analyserequation:
_analyserequation.AnalyserEquationVector_swigregister(AnalyserEquationVector)


# libCellML generated wrapper code starts here.

class AnalyserEquation(object):
    r"""Creates an :class:`AnalyserEquation` object."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    Type_TRUE_CONSTANT = _analyserequation.AnalyserEquation_Type_TRUE_CONSTANT
    Type_VARIABLE_BASED_CONSTANT = _analyserequation.AnalyserEquation_Type_VARIABLE_BASED_CONSTANT
    Type_RATE = _analyserequation.AnalyserEquation_Type_RATE
    Type_ALGEBRAIC = _analyserequation.AnalyserEquation_Type_ALGEBRAIC
    __swig_destroy__ = _analyserequation.delete_AnalyserEquation

    def type(self):
        r"""Returns the :enum:`AnalyserEquation::Type` for this :class:`AnalyserEquation` object."""
        return _analyserequation.AnalyserEquation_type(self)

    def ast(self):
        r"""Returns the :class:`AnalyserEquationAst` object for this :class:`AnalyserEquation` object."""
        return _analyserequation.AnalyserEquation_ast(self)

    def dependencies(self):
        r"""
        Returns the list of :class:`AnalyserEquation` objects which corresponds to the equations on which this
        :class:`AnalyserEquation` object depends.
        """
        return _analyserequation.AnalyserEquation_dependencies(self)

    def isStateRateBased(self):
        r"""Tests if this :class:`AnalyserEquation` object relies on states and/or rates."""
        return _analyserequation.AnalyserEquation_isStateRateBased(self)

    def variable(self):
        r"""Returns the :class:`AnalyserVariable` object for this :class:`AnalyserEquation` object."""
        return _analyserequation.AnalyserEquation_variable(self)

# Register AnalyserEquation in _analyserequation:
_analyserequation.AnalyserEquation_swigregister(AnalyserEquation)



