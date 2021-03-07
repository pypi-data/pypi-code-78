# -*- coding:utf-8; tab-width:4; mode:python -*-

import sys
import os
import argparse
import collections

import configobj

from .pattern import Bunch, MetaBunch

try:
    unicode
except NameError:
    unicode = str


def debug(msg):
    return
    print(msg)


class ArgumentConfigParser(argparse.ArgumentParser):
    def __init__(self, *args, **kargs):
        super(ArgumentConfigParser, self).__init__(*args, **kargs)

    def load_config_file(self, infile):
        if not os.path.exists(infile):
            debug("{} is not a file".format(infile))
            return

        self.load_config(open(infile).read().splitlines())

    def load_config(self, chunk):
        self._do_load_config(chunk)

    def parse_args(self, commandline=None, ns=None):
        self._update_casts()

        if commandline is None:
            commandline = sys.argv[1:]

        ns = ns or Bunch()
        new_values = argparse.ArgumentParser.parse_args(
            self, args=commandline, namespace=ns)

        debug("update from cli: {}".format(new_values))
        self._promote_config(new_values)
        debug("after promote: {}".format(args))

        return args

    def _do_load_config(self, config):
        new_config = configobj.ConfigObj(config)

        for name in new_config.sections:
            if name == 'ui':
                self._load_from_section(new_config.get('ui'))

            setattr(args, name, MetaBunch(new_config[name]))

    def _load_from_section(self, section):
        if section is None:
            return

        for key, value in section.items():
            if not key.startswith('cmd:'):
                args[key] = value
                continue

            command = key[4:]
            for key, val in value.items():
                fullkey = command + '_' + key
                args[fullkey] = val

    def _update_casts(self):
        for action in parser._actions:
            key = action.dest
            value = args.get(key)

            if value is None:
                continue

            value = self._cast_value(action, value)
            args[key] = value

    def _cast_value(self, action, value):
        if not isinstance(value, (str, unicode)) or action.type is None:
            return value

        debug("using '{}' to cast '{}'".format(action.type, value))

        try:
            value = action.type(value) if action.type and value is not None else value
        except ValueError:
            raise ValueError("Type mismatch for '{}' ({}) with value '{}'".format(
                action.dest, action.type.__name__, value))

        return value

    def _promote_config(self, src):
        for key, val in src.items():
            if key not in args:
                args[key] = None

            new_value = val
            val2 = self._promote_single(args.get(key), new_value)
            debug("promoting '{}' '{}' <= current '{}' new '{}'".format(
                key, val2, args.get(key), new_value))

            args[key] = val2

    def _promote_single(self, prev, new):
        """
        >>> promote({'default':1}, None)
        1
        >>> promote({'foo':2}, 'foo')
        2
        >>> promote({'foo':3}, 'other')
        'other'
        >>> promote('foo', 'other')
        'other'
        >>> promote('foo', None)
        'foo'
        >>> promote('None, 0)
        0
        """

        if isinstance(prev, collections.MutableMapping):
            if new in prev:
                return prev[new]
            if new is None:
                return prev['default']
            return new

        return new if new is not None else prev


class DebugBunch(MetaBunch):
    def __setitem__(self, key, value):
        debug("DebugBunch: {} = {}".format(key, value))
        MetaBunch.__setitem__(self, key, value)

args = DebugBunch()
parser = ArgumentConfigParser()
add_argument = parser.add_argument
