from pysfcgal.sfcgal import Point


def wkt_leak():
    while True:
        p = Point.from_wkt("POINT (1 2)")
        p.to_wkt()


if __name__ == "__main__":
    wkt_leak()
