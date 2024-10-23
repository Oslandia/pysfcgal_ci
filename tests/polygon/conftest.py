import pytest


@pytest.fixture
def big_ring():
    yield [(0., 0.), (10., 0.), (10., 10.), (0., 10.), (0., 0.)]


@pytest.fixture
def ring_around_0():
    yield [(-1., -1.), (1., -1.), (1., 1.), (-1., 1.), (-1., -1.)]


@pytest.fixture
def small_ring_23():
    yield [(2., 2.), (3., 2.), (3., 3.), (2., 2.)]


@pytest.fixture
def small_ring_56():
    yield [(5., 5.), (5., 6.), (6., 6.), (5., 5.)]
