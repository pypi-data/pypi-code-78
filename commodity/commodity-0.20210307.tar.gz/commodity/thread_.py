# -*- coding:utf-8; tab-width:4; mode:python -*-

import os
import time
import select
from threading import Thread
import logging
import locale
import random
random.seed()

try:
    import Queue
except ImportError:
    import queue as Queue


from .log import NullHandler

logger = logging.getLogger('commodity.thread')
logger.setLevel(logging.DEBUG)
logger.addHandler(NullHandler())
logger.propagate = False

from .pattern import memoized

from .type_ import checked_type

all = ['ReaderThread',
       'ThreadFunc',
       'start_new_thread',
       'SimpleThreadPool',
       'WorkerGroup']


def ReaderThread(fin, fout, text=False, encoding=None, errors=None):
    if fout is None:
        return DummyReaderThread()

    return ActualReaderThread(fin, fout, text, encoding, errors)


class DummyReaderThread(object):
    def flush(self):
        pass


class ActualReaderThread(Thread):
    """
    A thread that read from an actual file handler and write to an
    object that just has the write() method.
    """

    class Timeout(Exception):
        pass

    class EOF(Exception):
        pass

    def __init__(self, fdin, fdout, text=False, encoding=None, errors=None):
        super(ActualReaderThread, self).__init__()
        self.fdin = fdin
        self.fdout = fdout
        assert not fdout.closed, fdout
        self.text = text
        self.encoding = encoding or locale.getpreferredencoding(False)
        self.errors = errors or 'strict'
        self.running = True
        self.start()
        time.sleep(0.01)

    def _read_in(self, timeout=0.2):
        ready = select.select([self.fdin], [], [], timeout)[0]
        if not ready:
            raise self.Timeout

        data = os.read(self.fdin.fileno(), 2048)
        if not data:
            raise self.EOF

        return data

    def run(self):
        while self.running:
            try:
                data = self._read_in()

                if self.text:
                    data = data.decode(self.encoding, self.errors)

                try:
                    self.fdout.write(data)
                except TypeError:
                    if isinstance(data, str):
                        data = bytes(data, self.encoding, self.errors)
                    else:
                        data = data.decode(self.encoding, self.errors)
                    self.fdout.write(data)

            except self.Timeout:
                continue

            except self.EOF:
                break

    def flush(self):
        self.running = False
        self.join(2)
        while 1:
            try:
                self.fdout.write(self._read_in(timeout=0.5))
            except (self.Timeout, self.EOF):
                break

        self.fdout.flush()


class ThreadFunc(Thread):
    """
    Execute given function in a new thread. It provides return value (or exception) as
    object atribbutes.

    >>> import math

    >>> tf = ThreadFunc(math.sin, 8)
    >>> tf.join()
    >>> tf.result
    0.9893582466233818

    >>> tf = ThreadFunc(math.sqrt, -1)
    >>> tf.join()
    >>> tf.exception
    >>> ValueError('math domain error')
    """

    def __init__(self, target, *args, **kargs):
        self.target = target
        self.args = args
        self.kargs = kargs
        super(ThreadFunc, self).__init__()
        self.result = self.exception = None
        self.start()
        time.sleep(0.01)

    def run(self):
        try:
            self.result = self.target(*self.args, **self.kargs)
        except Exception as e:
            self.exception = e


def start_new_thread(target, *args, **kargs):
    """
    Execute given function in a new thread. It returns a :class:`ThreadFunc` object.
    """
    return ThreadFunc(target, *args, **kargs)


class SimpleThreadPool:
    """A generic and simple thread pool. Function return value are received by means of
    callbacks.

    >>> import math
    >>>
    >>> result = []
    >>> pool = SimpleThreadPool(4)
    >>> pool.add(math.pow, (1, 2), callback=result.append)
    >>> pool.join()

    Also implements a parallel :py:func:`map` for an argument sequence for a function executing each
    on a different thread:

    >>> pool = SimpleThreadPool(4)
    >>> pool.map(math.sqrt, ((2, 4, 5, 9)))
    (1.4142135623730951, 2.0, 2.23606797749979, 3.0)

    >>> pool.map(math.pow, [2, 3, 3], [2, 2, 4])
    (4, 9, 81)
    """
    def __init__(self, num_workers):
        self.tasks = Queue.Queue()
        self.threads = [SimpleThreadPool.Worker(self.tasks) for x in range(num_workers)]

    def add(self, func, args=(), kargs={}, callback=lambda x: x):
        assert callable(func)
        self.tasks.put((func, args, kargs, callback))

    def map(self, func, *sequences):
        if len(sequences) == 1:
            it = zip(sequences[0])
        else:
            it = zip(*sequences)

        holders = []

        for args in it:
            holder = SimpleThreadPool.Holder()
            holders.append(holder)
            self.add(func, args, {}, holder)

        self.join()

        return tuple(x.value for x in holders)

    def join(self):
        self.tasks.join()

    class Worker(Thread):
        def __init__(self, tasks):
            Thread.__init__(self)
            self.tasks = tasks
            self.daemon = True
            self.start()

        def run(self):
            while 1:
                try:
                    self.run_next()
                except Exception as e:
                    logger.critical("Worker: %s", e)
                    print(e)

        def run_next(self):
            func, args, kargs, callback = self.tasks.get()

            logger.debug("thread %s taken %s", self, func)
            result = func(*args, **kargs)
            self.tasks.task_done()

            callback(result)

    class Holder:
        def __init__(self):
            self.value = None

        def __call__(self, arg):
            self.value = arg


class WorkerGroup(object):
    """
    A group of dedicated workers.

    >>> import math
    >>>
    >>> results = []
    >>> group = WorkerGroup(4)
    >>> w1 = group.get_worker("some unique value")
    >>> w1.add(math.square, (9,), callback=results.append)
    >>> group.join()
    >>>
    >>> print results
    [81]
    """
    def __init__(self, num_workers):
        self.workers = [WorkerGroup.Worker(Queue.Queue()) for x in range(num_workers)]

    @memoized
    def get_worker(self, id_):
        return random.choice(self.workers)

    def join(self):
        for w in self.workers:
            w.tasks.join()

    class Worker(SimpleThreadPool.Worker):
        def add(self, func, args=(), kargs={}, callback=lambda x: x):
            assert callable(func)
            self.tasks.put((func, args, kargs, callback))
