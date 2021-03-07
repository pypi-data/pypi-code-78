# -*- coding:utf-8; tab-width:4; mode:python -*-

import sys
import os.path
import socket
import io
import shlex
import subprocess as sp
from subprocess import PIPE, STDOUT, DEVNULL
from subprocess import CalledProcessError  # to be exported
import signal
import errno
import time
import warnings

import logging

try:
    unicode
except NameError:
    unicode = str


from hamcrest import is_not

from .testing import wait_that, call_with
from .thread_ import ReaderThread
from .type_ import checked_type
from .path import resolve_path

from .log import NullHandler

__all__ = ['SubProcess', 'Pipe', 'resolve_path', PIPE, STDOUT, DEVNULL]

log = logging.getLogger('commodity.os')
log.addHandler(NullHandler())

BUFFER = -4  # same idea of subprocess PIPE, STDOUT and DEVNULL


def is_special_fd(fd):
    return isinstance(fd, (int, type(None)))


def get_arg(dct, name, default=None, cls=None):
    retval = dct.pop(name, default)
    if cls is not None:
        return checked_type(cls, retval)

    if default is not None:
        return checked_type(type(default), retval)

    return retval


class SubProcess(sp.Popen):
    """
    A specialization of :class:`subprocess.Popen` that accepts any file-like object as
    stdout, stderr arguments, including 'string based files' . It accepts all
    subprocess.Popen keywords too.

    >>> out = io.BytesIO()
    >>> SubProcess('echo hi', stdout=out).wait()
    >>> assert(out.getvalue().strip() == 'hi')
    """
    def __init__(self, command_line, **kargs):
        self.command = command_line

        if sys.version_info < (3, 0):
            if isinstance(command_line, unicode):
                command_line = command_line.encode('utf8')

        if isinstance(command_line, str):
            self.command = shlex.split(command_line)

        self.kargs = kargs

        self.outsink = get_arg(kargs, 'stdout')
        self.errsink = get_arg(kargs, 'stderr')
        self.shell   = get_arg(kargs, 'shell')
        self.log     = get_arg(kargs, 'logger', log)
        self._start  = get_arg(kargs, 'start',  True)
        self.signal  = get_arg(kargs, 'signal', signal.SIGTERM)
        self.close_outs = get_arg(kargs, 'close_outs', False)
        self.cwd = kargs.get('cwd')

        if self.shell:
            self.command = ['/bin/bash', '-c', "%s" % command_line]

        self.pid = None
        self._started = False
        self.returncode = None
        if self._start:
            self.start()

    def start(self):
        if self._started:
            return

        self._run()
        self._started = True

    def _run(self):
        def check_sink(sink):
            if is_special_fd(sink):
                return sink

            return sp.PIPE

        kargs = self.kargs.copy()
        if sys.version_info.minor < 7 and "text" in kargs:
            kargs.pop("text")

        super(SubProcess, self).__init__(
            self.command,
            stdout     = check_sink(self.outsink),
            stderr     = check_sink(self.errsink),
            close_fds  = True,
            preexec_fn = os.setsid,
            **kargs)

        self.stdout_reader = self.stderr_reader = None

        if not is_special_fd(self.outsink):
            self.stdout_reader = ReaderThread(self.stdout, self.outsink, self.kargs.get('text'))

        if not is_special_fd(self.errsink):
            self.stderr_reader = ReaderThread(self.stderr, self.errsink, self.kargs.get('text'))

    def wait(self, timeout=None, expected=None):
        self.start()

        if timeout:
            try:
                wait_that(self.poll, call_with().returns(is_not(None)), timeout=timeout)
            except AssertionError:
                self.terminate()
                raise

        super(SubProcess, self).wait()

        self.flush()

        if expected is not None:
            assert self.returncode == expected, '{} returns {}, but expected was {}'.format(self, self.returncode, expected)

        return self.returncode

    def flush(self):
        if self.stdout_reader:
            self.stdout_reader.flush()
        if self.stderr_reader:
            self.stderr_reader.flush()

        if self.close_outs:
            self._close_outs()

    def _close_outs(self):
        if hasattr(self.outsink, 'close'):
            self.outsink.close()
        if hasattr(self.errsink, 'close'):
            self.errsink.close()

    def terminated(self):
        return self.poll() is not None

    def terminate(self, signum=None, assure=True):
        """Send signal to process to terminate it.

        :param signum: Signal to kill the subprocess. If is `None`, SubProcess.signal is used.
        :type name: str.
        :param assure: When `True`, it sends signal until the process is actually terminated
        :type assure: bool.
        """
        if self.terminated():
            return

        signum = signum or self.signal

        try:
            self.log.debug("receives signal %s", signum)
            os.killpg(self.pid, signum)

        except OSError as e:
            if e.errno == errno.ESRCH:  # No such process
                return

            self.log.debug("%s (%s)" % (e, self.pid))
            return

        except AttributeError:
            self.log.warning("did not even start")
            return

        if not assure:
            return

        tini = time.time()
        while 1:
            if self.terminated():
                break

            time.sleep(0.5)
            difftime = time.time() - tini

            if difftime > 5:
                self.log.warning('is still alive after %.2f seconds!', difftime)
                self.terminate(signal.SIGKILL, assure=False)
                return

            if difftime > 3:
                self.terminate(signum, assure=False)

    def __repr__(self):
        pid = self.pid or '-'
        returncode = self.returncode
        if returncode is None:
            returncode = '-'

        cwd = ''
        if self.cwd:
            cwd = " cwd:'{}'".format(self.cwd)

        return "SubProcess: pid:{0} rcode:{1}{2} {3!r}".format(
            pid, returncode, cwd, str.join(' ', self.command))


def check_output(command, **kargs):
    kargs['stdout'] = out = io.BytesIO()
    kargs['stderr'] = err = io.BytesIO()

    ps = SubProcess(command, **kargs)
    ps.wait()

    if ps.returncode:
        ex = CalledProcessError(ps.returncode, str.join(' ', ps.command))
        ex.output = out.getvalue()
        ex.err = err.getvalue()
        raise ex

    return out.getvalue()


class Pipe:
    def __init__(self):
        a, b = socket.socketpair()
        self.read_end = a.makefile()
        self.write_end = b.makefile('wb', 0)


def remove_force(fpath):
    try:
        os.remove(fpath)
    except OSError:
        pass


class FileTee(object):
    def __init__(self, *fds):
        self.fds = fds

    def write(self, data):
        for fd in self.fds:
            fd.write(data)

    def flush(self):
        for fd in self.fds:
            fd.flush()

    @property
    def closed(self):
        return any(x.closed for x in self.fds)

    def close(self):
        for fd in self.fds:
            fd.close()

    def __repr__(self):
        return 'FileTee({0}) closed?:{1}'.format(list(self.fds), [x.closed for x in self.fds])


class LineStreamPrefixer(object):
    def __init__(self, fd, prefix):
        self.fd = fd
        self.prefix = prefix
        self.tag_active = True
        self.closed = False

    def write(self, text):
        if not text:
            return

        if self.tag_active:
            text = self.prefix + text
            self.tag_active = False

        out = text[:-1].replace('\n', '\n' + self.prefix) + text[-1]
        if text[-1] == '\n':
            self.put_tag = True

        self.fd.write("%s" % out)
        self.fd.flush()

    def flush(self):
        pass

    def isatty(self):
        return False

    def close(self):
        self.fd.close()


class FuncAsTextFile(object):
    def __init__(self, func, prefix=''):
        self.func = func
        self.prefix = prefix
        self.remain = ''
        self.closed = False

    def readable(self):
        return False

    def writable(self):
        return True

    def seekable(self):
        return False

    def write(self, text):
        text = self.remain + text
        self.remain = ''

        if not text:
            return

        lines = text.split('\n')
        if lines[-1]:
            self.remain = lines[-1]

        for line in lines[:-1]:
            self.func(self.prefix + line.rstrip())

    def flush(self):
        self.write('')

    def close(self):
        self.flush()


def FuncAsFile(func, prefix=''):
    warnings.warn("FuncAsFile is deprecated, use FuncAsTextFile", PendingDeprecationWarning)
    return FuncAsTextFile(func, prefix)


def LoggerAsFile(func, prefix=''):
    warnings.warn("LoggerAsFile is deprecated, use FuncAsTextFile", PendingDeprecationWarning)
    return FuncAsTextFile(func, prefix)


def wait_or_raise(predicate, delta=1, timeout=5, exc=AssertionError):
    """
    Poll (each 'delta' secs) until 'predicate' become True.
    If tiemout is reached, it raises 'exc'.
    """

    init = time.time()
    while 1:
        if predicate():
            break

        time.sleep(delta)
        if time.time() - init > timeout:
            raise exc("Predicate {0} was never satisfied after {1} secs".format(
                predicate, timeout))
