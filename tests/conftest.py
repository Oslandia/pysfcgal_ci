import shutil
import tempfile
from pathlib import Path

import pytest

tests_dir = Path(__file__).parent


@pytest.fixture
def tmp_test_dir():
    tmp_dir = tempfile.mkdtemp()
    yield Path(tmp_dir)
    shutil.rmtree(tmp_dir, ignore_errors=True)


@pytest.fixture
def c0():
    yield (0., 0., 0.)


@pytest.fixture
def c1():
    yield (1., 0., 0.)


@pytest.fixture
def c2():
    yield (0., 1., 0.)


@pytest.fixture
def c3():
    yield (0., 0., 1.)
