# -*- coding:utf-8; tab-width:4; mode:python -*-

import sys
import string
import tempfile


def add_prefix(prefix, items):
    '''
    Add a common prefix to all strings of a list:

    >>> add_prefix('pre-', ['black', 'red', 'orange'])
    ['pre-black', 'pre-red', 'pre-orange']
    '''
    return [prefix + i for i in items]


def convert_to_string(obj, encoding='utf-8'):
    '''
    Returns an encoded string from unicode or string.
    '''
    assert isinstance(obj, (str, unicode)), type(obj)

    if isinstance(obj, unicode):
        return obj.encode(encoding, 'replace')

    return obj


# FIXME: add an example in the docstring
class TreeRender(object):
    @classmethod
    def draw(cls, sequence, func, connector='', level=0, args=[]):
        retval = ''
        lon = len(sequence)
        for i, item in enumerate(sequence):
            brother = cls.norm_brother
            parent  = cls.norm_parent

            if lon == i + 1:
                brother = cls.last_brother
                parent  = cls.last_parent

            retval += func(item,
                           connector + parent,
                           connector + brother,
                           level + 1,
                           *args)

        return retval


class UTF_TreeRender(TreeRender):
    '''
    Draws an ASCII art tree with UTF characters.
    '''

    norm_brother = u'├─'
    last_brother = u'└─'
    norm_parent = u'│  '
    last_parent = u'   '


class ASCII_TreeRender(TreeRender):
    '''
    Draws an ASCII-art tree just with ASCII characters.
    norm_brother = '+-'
    '''
    last_brother = '`-'
    norm_parent = '|  '
    last_parent = '   '


class Printable(object):
    '''
    Class mixin that provides a __str__ method from the __unicode__ method.
    '''

    def __repr__(self):
        return str(self)

    def __str__(self):
        if sys.version_info < (3, 0):
            return unicode(self).encode('utf-8', 'replace')

        return self.__unicode__()

    def __unicode__(self):
        raise NotImplementedError


class TemplateFile(object):
    '''
    Render a template (given as string or input file) and renders it
    with a dict over a string, given filename or tempfile.

    >>> t = TemplateFile('$who likes $what')
    >>> t.render(dict(who='kate', what='rice'))
    'kate likes rice'
    '''

    def __init__(self, template):
        self.template = string.Template(template)

    @classmethod
    def from_file(self, filename):
        with file(filename) as fd:
            return TemplateFile(fd.read())

    def render(self, values):
        return self.template.substitute(**values)

    def render_to_file(self, values, filename):
        with file(filename, 'wt') as fd:
            fd.write(self.render(values))

    def render_to_tempfile(self, values):
        fd, filename = tempfile.mkstemp()
        self.render_to_file(values, filename)
        return filename
