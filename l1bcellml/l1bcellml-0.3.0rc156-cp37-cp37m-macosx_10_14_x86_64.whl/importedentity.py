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
    from . import _importedentity
else:
    import _importedentity

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


import libcellml.namedentity
import libcellml.entity
import libcellml.types

# libCellML generated wrapper code starts here.

class ImportedEntity(object):
    r"""Abstract base class for entities that can be imported."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _importedentity.delete_ImportedEntity

    def isImport(self):
        r"""Test if this entity is imported."""
        return _importedentity.ImportedEntity_isImport(self)

    def importSource(self):
        r"""Returns an ImportSource if this entity is imported, else `None`."""
        return _importedentity.ImportedEntity_importSource(self)

    def setImportSource(self, importSource):
        r"""Set the ImportSource for this entity (use `None` to unset)."""
        return _importedentity.ImportedEntity_setImportSource(self, importSource)

    def importReference(self):
        r"""
        Returns the reference to the entity in the imported model, or an empty string
        if not set.
        """
        return _importedentity.ImportedEntity_importReference(self)

    def setImportReference(self, reference):
        r"""
        Set the import reference to an entity in the imported model (use an empty
        string to unset).
        """
        return _importedentity.ImportedEntity_setImportReference(self, reference)

    def isResolved(self):
        return _importedentity.ImportedEntity_isResolved(self)

    def setResolved(self, status):
        return _importedentity.ImportedEntity_setResolved(self, status)

# Register ImportedEntity in _importedentity:
_importedentity.ImportedEntity_swigregister(ImportedEntity)



