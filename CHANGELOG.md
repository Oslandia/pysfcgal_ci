# PySFCGAL Changelog

## Version 1.5.2 (2024-07-25)

### New Features
- Add Solid high-level interface (!40, Raphaël Delhome)
- Add GeometryCollection high-level interface (!39, Raphaël Delhome)
- Add Triangle and Tin high-level interface (!38, Raphaël Delhome)
- Add PolyhedralSurface high-level interface (!37, Raphaël Delhome)
- Add Multi-geometries high-level interface (!33, Raphaël Delhome)
- Add Polygon high-level interface (!32, Raphaël Delhome)
- Add LineString high-level interface (!29, Raphaël Delhome)
- Add extrude (!17, Florent Fougères)
- Add VTK export (!18, Loïc Bartoletti)

### Improvements
- Fix a typo in tin_from_coordinates and add a test (!35, Loïc Bartoletti)
- Update wkb to handle binary and hex wkb (!23, Loïc Bartoletti)
- Improve installation documentation (!20, Florent Fougères)

### CI/CD
- Build windows wheel (!21, Jean Felder)
- Add a flake8 job (!26, Jean Felder)

### Tests
- Add force_lhr and force_rhr test (!34, Loïc Bartoletti)
- Fix visibility algorithm test (!24, Loïc Bartoletti)

### Other
- Switch to GPLv3+ (!22, Raphaël Delhome)

## Version 1.5.1 (2023-12-21)

### Improvements
- Update build instructions for Unix and add for Windows
- Add detection for MSVC bugs on CGAL
- Update sfcgal_def.c file to remove #if/#endif for MSVC

### Fixes
- Fix exception message for Python versions
- Update update_def.sh script to handle #if/#endif for MSVC/CGAL bugs on alpha shapes

### Other
- Replace gitlab.com/Oslandia with gitlab.com/SFCGAL

## Version 1.5.0 (2023-10-31)

### New Features
- Add support for visibility
- Add has_exterior_vertex method for polygons
- Add Python bindings support for straight skeleton extrusion
- Add WKB read/write
- Add partition function
- Add high-level interface for Polygon

### Improvements
- Modernize property declarations
- Update SFCGAL C API

### Fixes
- Fix parameters in partition contracts
- Fix crash in wrap_geom

### Tests
- Add tests for straight skeleton extrusion and visibility

## Version 1.4.1 (2022-01-27)

### New Features
- Add linesubstring and alpha_shapes
- Add sfcgal_full_version
- Add convexhull and convexhull_3D
- Add polyhedral_surface
- Add intersects_3d and intersection_3d
- Add union and union_3d

### Improvements
- Use typing and minor fixes
- Import icontract for DbC (Design by Contract)
- Add missing methods (line_sub_string, orientation, is_planar, covers_3d, volume for solids)
- Improve point constructor with m value

### Dependencies
- Add icontract as a dependency

### Tests
- Add numerous tests for new features

### Other
- Align version with SFCGAL

## Version 0.1.0 (2020-07-27)

### New Features
- Add minkowski_sum, straight_skeleton, and others
- Add TIN and triangulation support
- Add difference and force_{l,r}hr
- Add Point.z and Point.has_z properties
- Add access to linestring coordinates
- Add access to geometry collection geometries via .geoms

### CI/CD
- Add Cirrus CI

### Fixes
- Fix memory leaks
- Fix path for ffibuilder

### Other
- Initial project commit
