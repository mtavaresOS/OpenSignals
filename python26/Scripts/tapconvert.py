#!c:\python26\python.exe
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.
import sys

try:
    import _preamble
except ImportError:
    sys.exc_clear()

from twisted.scripts.tapconvert import run
run()