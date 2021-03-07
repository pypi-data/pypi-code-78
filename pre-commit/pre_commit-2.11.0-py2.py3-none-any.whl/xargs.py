import concurrent.futures
import contextlib
import math
import os
import subprocess
import sys
from typing import Any
from typing import Callable
from typing import Generator
from typing import Iterable
from typing import List
from typing import MutableMapping
from typing import Optional
from typing import Sequence
from typing import Tuple
from typing import TypeVar

from pre_commit import parse_shebang
from pre_commit.util import cmd_output_b
from pre_commit.util import cmd_output_p

TArg = TypeVar('TArg')
TRet = TypeVar('TRet')


def _environ_size(_env: Optional[MutableMapping[str, str]] = None) -> int:
    environ = _env if _env is not None else getattr(os, 'environb', os.environ)
    size = 8 * len(environ)  # number of pointers in `envp`
    for k, v in environ.items():
        size += len(k) + len(v) + 2  # c strings in `envp`
    return size


def _get_platform_max_length() -> int:  # pragma: no cover (platform specific)
    if os.name == 'posix':
        maximum = os.sysconf('SC_ARG_MAX') - 2048 - _environ_size()
        maximum = max(min(maximum, 2 ** 17), 2 ** 12)
        return maximum
    elif os.name == 'nt':
        return 2 ** 15 - 2048  # UNICODE_STRING max - headroom
    else:
        # posix minimum
        return 2 ** 12


def _command_length(*cmd: str) -> int:
    full_cmd = ' '.join(cmd)

    # win32 uses the amount of characters, more details at:
    # https://github.com/pre-commit/pre-commit/pull/839
    if sys.platform == 'win32':
        return len(full_cmd.encode('utf-16le')) // 2
    else:
        return len(full_cmd.encode(sys.getfilesystemencoding()))


class ArgumentTooLongError(RuntimeError):
    pass


def partition(
        cmd: Sequence[str],
        varargs: Sequence[str],
        target_concurrency: int,
        _max_length: Optional[int] = None,
) -> Tuple[Tuple[str, ...], ...]:
    _max_length = _max_length or _get_platform_max_length()

    # Generally, we try to partition evenly into at least `target_concurrency`
    # partitions, but we don't want a bunch of tiny partitions.
    max_args = max(4, math.ceil(len(varargs) / target_concurrency))

    cmd = tuple(cmd)
    ret = []

    ret_cmd: List[str] = []
    # Reversed so arguments are in order
    varargs = list(reversed(varargs))

    total_length = _command_length(*cmd) + 1
    while varargs:
        arg = varargs.pop()

        arg_length = _command_length(arg) + 1
        if (
                total_length + arg_length <= _max_length and
                len(ret_cmd) < max_args
        ):
            ret_cmd.append(arg)
            total_length += arg_length
        elif not ret_cmd:
            raise ArgumentTooLongError(arg)
        else:
            # We've exceeded the length, yield a command
            ret.append(cmd + tuple(ret_cmd))
            ret_cmd = []
            total_length = _command_length(*cmd) + 1
            varargs.append(arg)

    ret.append(cmd + tuple(ret_cmd))

    return tuple(ret)


@contextlib.contextmanager
def _thread_mapper(maxsize: int) -> Generator[
    Callable[[Callable[[TArg], TRet], Iterable[TArg]], Iterable[TRet]],
    None, None,
]:
    if maxsize == 1:
        yield map
    else:
        with concurrent.futures.ThreadPoolExecutor(maxsize) as ex:
            yield ex.map


def xargs(
        cmd: Tuple[str, ...],
        varargs: Sequence[str],
        *,
        color: bool = False,
        target_concurrency: int = 1,
        _max_length: int = _get_platform_max_length(),
        **kwargs: Any,
) -> Tuple[int, bytes]:
    """A simplified implementation of xargs.

    color: Make a pty if on a platform that supports it
    target_concurrency: Target number of partitions to run concurrently
    """
    cmd_fn = cmd_output_p if color else cmd_output_b
    retcode = 0
    stdout = b''

    try:
        cmd = parse_shebang.normalize_cmd(cmd)
    except parse_shebang.ExecutableNotFoundError as e:
        return e.to_output()[:2]

    # on windows, batch files have a separate length limit than windows itself
    if (
            sys.platform == 'win32' and
            cmd[0].lower().endswith(('.bat', '.cmd'))
    ):  # pragma: win32 cover
        # this is implementation details but the command gets translated into
        # full/path/to/cmd.exe /c *cmd
        cmd_exe = parse_shebang.find_executable('cmd.exe')
        _max_length = 8192 - len(cmd_exe) - len(' /c ')

    partitions = partition(cmd, varargs, target_concurrency, _max_length)

    def run_cmd_partition(
            run_cmd: Tuple[str, ...],
    ) -> Tuple[int, bytes, Optional[bytes]]:
        return cmd_fn(
            *run_cmd, retcode=None, stderr=subprocess.STDOUT, **kwargs,
        )

    threads = min(len(partitions), target_concurrency)
    with _thread_mapper(threads) as thread_map:
        results = thread_map(run_cmd_partition, partitions)

        for proc_retcode, proc_out, _ in results:
            retcode = max(retcode, proc_retcode)
            stdout += proc_out

    return retcode, stdout
