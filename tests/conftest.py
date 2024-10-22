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


@pytest.fixture
def ring1():
    yield [(0., 0.), (10., 0.), (10., 10.), (0., 10.), (0., 0.)]


@pytest.fixture
def ring2():
    yield [(-1., -1.), (1., -1.), (1., 1.), (-1., 1.), (-1., -1.)]


@pytest.fixture
def ring3():
    yield [(2., 2.), (3., 2.), (3., 3.), (2., 2.)]


@pytest.fixture
def ring4():
    yield [(5., 5.), (5., 6.), (6., 6.), (5., 5.)]
