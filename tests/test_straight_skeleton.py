import pytest

from pysfcgal.sfcgal import Polygon


@pytest.mark.parametrize(
    "poly_wkt, nb_output_geometries, expected_wkt",
    [
        [
            "POLYGON ((0 0, 0 2, 1 2, 1 1, 2 1, 2 0, 0 0))",
            6,
            (
                "MULTIPOLYGON (((0.00 0.00,0.50 0.50,0.50 1.50,0.00 2.00)),((2.00 "
                "0.00,1.50 0.50,0.50 0.50,0.00 0.00)),((2.00 1.00,1.50 0.50,2.00 "
                "0.00)),((1.00 1.00,0.50 0.50,1.50 0.50,2.00 1.00)),((1.00 2.00,0.50 "
                "1.50,0.50 0.50,1.00 1.00)),((0.00 2.00,0.50 1.50,1.00 2.00)))"
            ),
        ],
        [
            "TRIANGLE ((0 0, 0 2, 1 2, 0 0))",
            3,
            (
                "MULTIPOLYGON (((0.00 0.00,0.38 1.62,0.00 2.00)),"
                "((1.00 2.00,0.38 1.62,0.00 0.00)),((0.00 2.00,0.38 1.62,1.00 2.00)))"
            ),
        ],
        [
            "POLYGON ((0 0, 0 2, 3 2, 3 0, 0 0))",
            4,
            (
                "MULTIPOLYGON (((0.00 0.00,1.00 1.00,0.00 2.00)),((3.00 0.00,2.00 "
                "1.00,1.00 1.00,0.00 0.00)),((3.00 2.00,2.00 1.00,3.00 0.00)),((0.00 "
                "2.00,1.00 1.00,2.00 1.00,3.00 2.00)))"
            ),
        ],
        [
            "POLYGON ((0 0, 0 3, 1 3, 1 2, 2 2, 2 3, 3 3, 3 0, 0 0))",
            8,
            (
                "MULTIPOLYGON (((0.00 0.00,1.00 1.00,0.50 1.50,0.50 2.50,0.00 "
                "3.00)),((3.00 0.00,2.00 1.00,1.00 1.00,0.00 0.00)),((3.00 3.00,2.50 "
                "2.50,2.50 1.50,2.00 1.00,3.00 0.00)),((2.00 3.00,2.50 2.50,3.00 "
                "3.00)),((2.00 2.00,2.50 1.50,2.50 2.50,2.00 3.00)),((1.00 2.00,0.50 "
                "1.50,1.00 1.00,2.00 1.00,2.50 1.50,2.00 2.00)),((1.00 3.00,0.50 "
                "2.50,0.50 1.50,1.00 2.00)),((0.00 3.00,0.50 2.50,1.00 3.00)))"
            ),
        ],
        [
            "POLYGON ((0 0, 0 4, 4 4, 4 0, 0 0), (1 1, 3 1, 3 3, 1 3, 1 1))",
            8,
            (
                "MULTIPOLYGON (((0.00 0.00,0.50 0.50,0.50 3.50,0.00 4.00)),((4.00 "
                "0.00,3.50 0.50,0.50 0.50,0.00 0.00)),((4.00 4.00,3.50 3.50,3.50 "
                "0.50,4.00 0.00)),((0.00 4.00,0.50 3.50,3.50 3.50,4.00 4.00)),((1.00 "
                "1.00,0.50 0.50,3.50 0.50,3.00 1.00)),((1.00 3.00,0.50 3.50,0.50 "
                "0.50,1.00 1.00)),((3.00 3.00,3.50 3.50,0.50 3.50,1.00 3.00)),((3.00 "
                "1.00,3.50 0.50,3.50 3.50,3.00 3.00)))"
            ),
        ],
        [
            "MULTIPOLYGON (((0 0, 0 2, 2 2, 2 0, 0 0)), ((3 3, 3 5, 5 5, 5 3, 3 3)))",
            8,
            (
                "MULTIPOLYGON (((0.00 0.00,1.00 1.00,0.00 2.00)),((2.00 0.00,1.00 "
                "1.00,0.00 0.00)),((2.00 2.00,1.00 1.00,2.00 0.00)),((0.00 2.00,1.00 "
                "1.00,2.00 2.00)),((3.00 3.00,4.00 4.00,3.00 5.00)),((5.00 3.00,4.00 "
                "4.00,3.00 3.00)),((5.00 5.00,4.00 4.00,5.00 3.00)),((3.00 5.00,4.00 "
                "4.00,5.00 5.00)))"
            ),
        ],
        [
            "POLYGON EMPTY",
            0,
            "MULTIPOLYGON EMPTY",
        ],
    ],
)
def test_straight_skeleton_partition(poly_wkt, nb_output_geometries, expected_wkt):
    polygon = Polygon.from_wkt(poly_wkt)
    assert polygon.is_valid()
    partition = polygon.straight_skeleton_partition()
    assert partition.geom_type == "MultiPolygon"
    assert len(partition) == nb_output_geometries
    assert partition.to_wkt(2) == expected_wkt