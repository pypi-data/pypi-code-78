#!/usr/bin/env python3

"""For doctests: We put a link in "tests" that points to "nourish". We make the symlink in "tests/doctests" instead
of directly under "tests" to avoid "tests/nourish" being imported during the tests and coverage won't be able to detect
coverage. This script is executed in tox.ini and should only be run from the project root."""

from pathlib import Path


path = Path("tests/doctests/nourish")

# We always try to clean up "tests/doctests/nourish" in case an outdated symlink is there (e.g., source directory being
# moved).
if path.exists():
    path.unlink()

path.parent.mkdir(exist_ok=True)
# We use a symlink to the absolute path to avoid potential system compatibility issues.
path.symlink_to(Path.cwd() / "nourish", target_is_directory=True)
