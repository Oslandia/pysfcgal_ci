import pytest

from pysfcgal.sfcgal import LineString, PolyhedralSurface, Solid, has_icontract

if has_icontract:
    import icontract


def test_solid(
    solid_1, expected_polyhedralsurfaces, solid_without_holes, solid_unordered
):
    assert solid_1.n_shells == 3
    # iteration
    for shell, expected_polyhedral in zip(solid_1, expected_polyhedralsurfaces):
        assert shell == expected_polyhedral
    # indexing
    for idx in range(solid_1.n_shells):
        solid_1[idx] == expected_polyhedralsurfaces[idx]
    solid_1[-1] == expected_polyhedralsurfaces[-1]
    solid_1[1:3] == expected_polyhedralsurfaces[1:3]
    # equality
    assert solid_1 != solid_without_holes
    assert solid_1 != solid_unordered


def test_solid_to_polyhedralsurface(solid_1, composed_polyhedralsurface):
    phs = solid_1.to_polyhedralsurface(wrapped=True)
    assert not phs.is_valid()  # PolyhedralSurface with interior shells
    assert phs.geom_type == "PolyhedralSurface"
    assert phs == composed_polyhedralsurface


def test_solid_to_coordinates(solid_1, points_ext_1, points_int_1_1, points_int_2_1):
    assert solid_1.to_coordinates() == [points_ext_1, points_int_1_1, points_int_2_1]
    other_solid = Solid.from_coordinates(solid_1.to_coordinates())
    assert other_solid == solid_1


def test_solid_to_dict(solid_1):
    solid_data = solid_1.to_dict()
    other_solid = Solid.from_dict(solid_data)
    assert other_solid == solid_1


def test_solid_set_exterior_shell(
        solid_1, points_ext_1, points_ext_2, c000, c100, c010):
    new_exterior_shell = PolyhedralSurface(points_ext_2)

    assert solid_1.n_shells == 3
    assert solid_1.shells[0] == PolyhedralSurface(points_ext_1)
    assert new_exterior_shell not in solid_1

    solid_1.set_exterior_shell(new_exterior_shell)
    assert solid_1.n_shells == 3
    assert solid_1.shells[0] == new_exterior_shell

    # try to set a linestring as exterior shell
    if has_icontract:
        with pytest.raises(icontract.errors.ViolationError):
            solid_1.set_exterior_shell(LineString([c000, c100, c010]))


def test_solid_add_interior_shell(
        solid_1, points_ext_1, points_ext_2, c000, c100, c010):
    new_interior_shell = PolyhedralSurface(points_ext_2)

    assert solid_1.n_shells == 3
    assert new_interior_shell not in solid_1

    solid_1.add_interior_shell(new_interior_shell)
    assert solid_1.n_shells == 4
    assert solid_1.shells[3] == new_interior_shell

    # try to add a linestring as interiro shell
    if has_icontract:
        with pytest.raises(icontract.errors.ViolationError):
            solid_1.add_interior_shell(LineString([c000, c100, c010]))
