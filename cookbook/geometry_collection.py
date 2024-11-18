from pysfcgal import sfcgal

point = sfcgal.Point(1, 3)
linestring = sfcgal.LineString([(1, 3), (3, 1)])
polygon = sfcgal.polygon([(1, 3),  (3, 3), (3, 1), (1, 1), (1, 3)])

collection = sfcgal.GeometryCollection()

collection.addGeometry(point)
collection.addGeometry(linestring)
collection.addGeometry(polygon)
