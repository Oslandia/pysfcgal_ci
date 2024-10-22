import pytest

from pysfcgal.sfcgal import MultiPolygon, Polygon


@pytest.fixture
def multipolygon(ring1, ring3, ring4):
    yield MultiPolygon([[ring1], [ring3], [ring4]])


@pytest.fixture
def other_multipolygon(ring1, ring3, ring2):
    yield MultiPolygon([[ring1], [ring3], [ring2]])


@pytest.fixture
def multipolygon_unordered(ring1, ring3, ring4):
    yield MultiPolygon([[ring4], [ring1], [ring3]])


@pytest.fixture
def expected_polygons(ring1, ring3, ring4):
    yield [Polygon(ring1), Polygon(ring3), Polygon(ring4)]


def test_multipolygon_iteration(multipolygon, expected_polygons):
    for polygon, expected_polygon in zip(multipolygon, expected_polygons):
        assert polygon == expected_polygon


def test_multipolygon_indexing(multipolygon, expected_polygons):
    for idx in range(len(multipolygon)):
        assert multipolygon[idx] == expected_polygons[idx]
    assert multipolygon[-1] == expected_polygons[-1]
    assert multipolygon[1:3] == expected_polygons[1:3]


def test_multipolygon_equality(
    multipolygon, other_multipolygon, multipolygon_unordered
):
    assert multipolygon != other_multipolygon
    assert multipolygon != multipolygon_unordered  # the order is important


def test_multipolygon_to_coordinates(multipolygon, ring1, ring3, ring4):
    assert multipolygon.to_coordinates() == [[ring1], [ring3], [ring4]]
    cloned_multipolygon = MultiPolygon(multipolygon.to_coordinates())
    assert cloned_multipolygon == multipolygon
    other_multipolygon = MultiPolygon.from_coordinates(multipolygon.to_coordinates())
    assert other_multipolygon == multipolygon


def test_multipolygon_to_dict(multipolygon):
    multipolygon_data = multipolygon.to_dict()
    other_multipolygon = MultiPolygon.from_dict(multipolygon_data)
    assert other_multipolygon == multipolygon
