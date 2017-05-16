import sys
from contextlib import contextmanager


class ProgressLogger:

    def __init__(self, progress):
        self.progress = progress

    def write(self, msg):
        self.progress.setConsoleInfo(msg)


@contextmanager
def redirect_stdout(progress):
    oldout = sys.stdout
    sys.stdout = ProgressLogger(progress)
    try:
        yield
    finally:
        sys.stdout = oldout
