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
    from Lib.pymj_core import _pymj_core
else:
    import _pymj_core

import builtins as __builtin__

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


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pymj_core.delete_SwigPyIterator

    def value(self):
        return _pymj_core.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pymj_core.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pymj_core.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pymj_core.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pymj_core.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pymj_core.SwigPyIterator_copy(self)

    def next(self):
        return _pymj_core.SwigPyIterator_next(self)

    def __next__(self):
        return _pymj_core.SwigPyIterator___next__(self)

    def previous(self):
        return _pymj_core.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pymj_core.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pymj_core.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pymj_core.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pymj_core.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pymj_core.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pymj_core.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pymj_core.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _pymj_core:
_pymj_core.SwigPyIterator_swigregister(SwigPyIterator)

class map_string_string(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pymj_core.map_string_string_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pymj_core.map_string_string___nonzero__(self)

    def __bool__(self):
        return _pymj_core.map_string_string___bool__(self)

    def __len__(self):
        return _pymj_core.map_string_string___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _pymj_core.map_string_string___getitem__(self, key)

    def __delitem__(self, key):
        return _pymj_core.map_string_string___delitem__(self, key)

    def has_key(self, key):
        return _pymj_core.map_string_string_has_key(self, key)

    def keys(self):
        return _pymj_core.map_string_string_keys(self)

    def values(self):
        return _pymj_core.map_string_string_values(self)

    def items(self):
        return _pymj_core.map_string_string_items(self)

    def __contains__(self, key):
        return _pymj_core.map_string_string___contains__(self, key)

    def key_iterator(self):
        return _pymj_core.map_string_string_key_iterator(self)

    def value_iterator(self):
        return _pymj_core.map_string_string_value_iterator(self)

    def __setitem__(self, *args):
        return _pymj_core.map_string_string___setitem__(self, *args)

    def asdict(self):
        return _pymj_core.map_string_string_asdict(self)

    def __init__(self, *args):
        _pymj_core.map_string_string_swiginit(self, _pymj_core.new_map_string_string(*args))

    def empty(self):
        return _pymj_core.map_string_string_empty(self)

    def size(self):
        return _pymj_core.map_string_string_size(self)

    def swap(self, v):
        return _pymj_core.map_string_string_swap(self, v)

    def begin(self):
        return _pymj_core.map_string_string_begin(self)

    def end(self):
        return _pymj_core.map_string_string_end(self)

    def rbegin(self):
        return _pymj_core.map_string_string_rbegin(self)

    def rend(self):
        return _pymj_core.map_string_string_rend(self)

    def clear(self):
        return _pymj_core.map_string_string_clear(self)

    def get_allocator(self):
        return _pymj_core.map_string_string_get_allocator(self)

    def count(self, x):
        return _pymj_core.map_string_string_count(self, x)

    def erase(self, *args):
        return _pymj_core.map_string_string_erase(self, *args)

    def find(self, x):
        return _pymj_core.map_string_string_find(self, x)

    def lower_bound(self, x):
        return _pymj_core.map_string_string_lower_bound(self, x)

    def upper_bound(self, x):
        return _pymj_core.map_string_string_upper_bound(self, x)
    __swig_destroy__ = _pymj_core.delete_map_string_string

# Register map_string_string in _pymj_core:
_pymj_core.map_string_string_swigregister(map_string_string)


def cutAnalyze(s):
    return _pymj_core.cutAnalyze(s)


