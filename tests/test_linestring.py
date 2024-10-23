import pytest

from pysfcgal.sfcgal import LineString


@pytest.fixture
def line(c000, c100, c010):
    yield LineString([c000, c100, c010])


@pytest.fixture
def line2(c000, c100, c001):
    yield LineString([c000, c100, c001])


@pytest.fixture
def long_line(c000, c100, c010, c001):
    yield LineString([c000, c100, c010, c001])


@pytest.mark.parametrize(
    "linestring,expected_length", [("line", 4), ("long_line", 9)],
)
def test_linestring_len(linestring, expected_length):
    assert len(linestring) == expected_length


def test_linestring_to_coordinates(long_line, c000, c100, c010, c001):
    coords = long_line.to_coordinates()
    assert len(coords) == 4
    assert coords[0] == c000
    assert coords[-1] == c001
    assert coords[0:2] == [c000, c100]
    cloned_linestring = LineString(coords)
    assert cloned_linestring == long_line
    other_linestring = LineString.from_coordinates(coords)
    assert other_linestring == long_line


def test_linestring_to_dict(long_line):
    linestring_data = long_line.to_dict()
    other_line = LineString.from_dict(linestring_data)
    assert other_line == long_line


def test_linestring_eq(line, line2):
    assert line != line2
    assert line != line2[:-1]
    assert line[:-1] == line2[:-1]


def test_linestring_getter(line):
    # Indexing with a wrong type
    with pytest.raises(TypeError):
        _ = line["cant-index-with-a-string"]
    # Positive indexing
    for idx, p in enumerate(line):
        assert line[idx] == p
    with pytest.raises(IndexError):
        _ = line[99]
    # Negative indexing
    for idx, p in enumerate(reversed(line)):
        assert line[-(idx + 1)] == p
    with pytest.raises(IndexError):
        _ = line[-99]
    # Slicing
    start_index = 1
    points = line[start_index:start_index+2]
    for idx, p in enumerate(points):
        assert p == line[start_index+idx]
