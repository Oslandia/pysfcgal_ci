import pytest

from pysfcgal.sfcgal import Polygon, PolyhedralSurface


@pytest.fixture
def polyhedralsurface(c0, c1, c2, c3):
    yield PolyhedralSurface(
        [[[c0, c1, c2]], [[c0, c1, c3]], [[c0, c2, c3]], [[c1, c2, c3]]]
    )


@pytest.fixture
def other_polyhedralsurface(c0, c1, c2, c3):
    yield PolyhedralSurface(
        [[[c0, c1, c2]], [[c0, c1, c3]], [[c0, c2, c3]]]
    )


@pytest.fixture
def polyhedralsurface_unordered(c0, c1, c2, c3):
    yield PolyhedralSurface(
        [[[c1, c2, c3]], [[c0, c1, c2]], [[c0, c1, c3]], [[c0, c2, c3]]]
    )


@pytest.fixture
def expected_polygons(c0, c1, c2, c3):
    yield [
        Polygon([c0, c1, c2]),
        Polygon([c0, c1, c3]),
        Polygon([c0, c2, c3]),
        Polygon([c1, c2, c3]),
    ]


def test_polyhedralsurface_len(polyhedralsurface):
    assert len(polyhedralsurface) == 4


def test_polyhedralsurface_iteration(polyhedralsurface, expected_polygons):
    for polygon, expected_polygon in zip(polyhedralsurface, expected_polygons):
        assert polygon == expected_polygon


def test_polyhedralsurface_indexing(polyhedralsurface, expected_polygons):
    for idx in range(len(polyhedralsurface)):
        assert polyhedralsurface[idx] == expected_polygons[idx]
    assert polyhedralsurface[-1] == expected_polygons[-1]
    assert polyhedralsurface[1:3] == expected_polygons[1:3]


def test_polyhedralsurface_equality(
    polyhedralsurface, other_polyhedralsurface, polyhedralsurface_unordered
):
    assert not other_polyhedralsurface.is_valid()
    assert polyhedralsurface != other_polyhedralsurface
    assert polyhedralsurface != polyhedralsurface_unordered


def test_polyhedralsurface_to_coordinates(polyhedralsurface, c0, c1, c2, c3):
    assert polyhedralsurface.to_coordinates() == [
        [[c0, c1, c2, c0]], [[c0, c1, c3, c0]], [[c0, c2, c3, c0]], [[c1, c2, c3, c1]]
    ]
    other_phs = PolyhedralSurface.from_coordinates(polyhedralsurface.to_coordinates())
    assert other_phs == polyhedralsurface


def test_polyhedralsurface_to_dict(polyhedralsurface):
    polyhedralsurface_data = polyhedralsurface.to_dict()
    other_polyhedralsurface = PolyhedralSurface.from_dict(polyhedralsurface_data)
    assert other_polyhedralsurface == polyhedralsurface


def test_to_solid():
    coords_str = (
        "((3.0 3.0 0.0,3.0 8.0 0.0,8.0 8.0 0.0,8.0 3.0 0.0"
        ",3.0 3.0 0.0)),"
        "((3.0 3.0 30.0,8.0 3.0 30.0,8.0 8.0 30.0,3.0 8.0 30.0,3.0 3.0 30.0)),"
        "((3.0 3.0 0.0,3.0 3.0 30.0,3.0 8.0 30.0,3.0 8.0 0.0,3.0 3.0 0.0)),"
        "((3.0 8.0 0.0,3.0 8.0 30.0,8.0 8.0 30.0,8.0 8.0 0.0,3.0 8.0 0.0)),"
        "((8.0 8.0 0.0,8.0 8.0 30.0,8.0 3.0 30.0,8.0 3.0 0.0,8.0 8.0 0.0)),"
        "((8.0 3.0 0.0,8.0 3.0 30.0,3.0 3.0 30.0,3.0 3.0 0.0,8.0 3.0 0.0))"
    )

    wkt_poly = f"POLYHEDRALSURFACE Z ({coords_str})"
    poly = PolyhedralSurface.from_wkt(wkt_poly)
    solid = poly.to_solid()
    expected_wkt = f"SOLID Z (({coords_str}))"
    assert solid.to_wkt(1) == expected_wkt
