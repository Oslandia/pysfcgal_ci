import shutil
import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def tmp_test_dir():
    tmp_dir = tempfile.mkdtemp()
    yield Path(tmp_dir)
    shutil.rmtree(tmp_dir, ignore_errors=True)


@pytest.fixture
def c000():
    yield (0., 0., 0.)


@pytest.fixture
def c100():
    yield (1., 0., 0.)


@pytest.fixture
def c010():
    yield (0., 1., 0.)


@pytest.fixture
def c001():
    yield (0., 0., 1.)
