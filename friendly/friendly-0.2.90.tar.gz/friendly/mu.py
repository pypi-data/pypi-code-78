import sys

exc_hook_name = repr(sys.excepthook)

if "InteractiveShell" in exc_hook_name:
    from .ipython import *  # noqa  Will automatically install

else:
    from friendly.console_helpers import *  # noqa
    from friendly.console_helpers import helpers  # noqa
    from friendly import install, run  # noqa

    __all__ = list(helpers.keys())
    __all__.append("install")
    __all__.append("run")


del exc_hook_name
del sys
