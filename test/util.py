import sys
from contextlib import contextmanager
from io import StringIO
from io import TextIOWrapper, BytesIO


class FakeResponse:
    def __init__(self, status_code: int, headers: dict):
        self.status_code = status_code
        self.headers = headers


@contextmanager
def captured_output():
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = StringIO(), StringIO()
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


@contextmanager
def captured_binary_output():
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = \
            TextIOWrapper(BytesIO(), sys.stdout.encoding), \
            TextIOWrapper(BytesIO(), sys.stderr.encoding)
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
