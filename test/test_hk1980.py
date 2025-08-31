from hk1980 import HK80, LatLon


class TestLatLon:
    def test_valid_contruction(self, valid_wgs84_point: tuple) -> LatLon:
        point_with_tuple = LatLon(*valid_wgs84_point, on_error="raise")
        point_with_clear_spec = LatLon(
            latitude=valid_wgs84_point[0],
            longitude=valid_wgs84_point[1],
            on_error="raise",
        )
        return point_with_clear_spec

    def test_invalid_construction(self, invalid_wgs84_point: tuple) -> LatLon:
        return LatLon(*invalid_wgs84_point)

    def test_conversion(self, valid_wgs84_point: tuple) -> HK80:
        LatLonObj = self.test_valid_contruction(valid_wgs84_point)
        return LatLonObj.to_hk80()

    def test_boundary_min_conversion(self, min_wgs84_point: tuple) -> HK80:
        LatLonObj = self.test_valid_contruction(min_wgs84_point)
        return LatLonObj.to_hk80()

    def test_boundary_max_conversion(self, max_wgs84_point: tuple) -> HK80:
        LatLonObj = self.test_valid_contruction(max_wgs84_point)
        return LatLonObj.to_hk80()


class TestHK80:
    def test_valid_contruction(self, valid_hk80_point: tuple) -> HK80:
        point_with_tuple = HK80(*valid_hk80_point, on_error="raise")
        point_with_clear_spec = HK80(
            easting=valid_hk80_point[0], northing=valid_hk80_point[1], on_error="raise"
        )
        return point_with_clear_spec

    def test_invalid_construction(self, invalid_hk80_point: tuple) -> HK80:
        return HK80(*invalid_hk80_point)

    def test_conversion(self, valid_hk80_point: tuple) -> LatLon:
        HK80Obj = self.test_valid_contruction(valid_hk80_point)
        return HK80Obj.to_wgs84()

    def test_boundary_min_conversion(self, min_hk80_point: tuple) -> LatLon:
        HK80Obj = self.test_valid_contruction(min_hk80_point)
        return HK80Obj.to_wgs84()

    def test_boundary_max_conversion(self, max_hk80_point: tuple) -> LatLon:
        HK80Obj = self.test_valid_contruction(max_hk80_point)
        return HK80Obj.to_wgs84()


def test_correct_conversion_to_wgs1984(valid_hk80_point, valid_wgs84_point):
    converted = HK80(*valid_hk80_point).to_wgs84()

    # response from https://www.geodetic.gov.hk/transform/v2/?inSys=hkgrid&e=813259.7&n=818940.16
    expected = {
        "wgsLat": 22.309278113,
        "wgsLong": 113.953573028,
    }

    ACCEPTED_TOLERANCE = 0.1
    assert abs(converted.latitude - expected["wgsLat"]) <= ACCEPTED_TOLERANCE
    assert abs(converted.longitude - expected["wgsLong"]) <= ACCEPTED_TOLERANCE


def test_correct_conversion_to_hk1980(valid_wgs84_point):
    converted = LatLon(*valid_wgs84_point).to_hk80()

    # response from https://www.geodetic.gov.hk/transform/v2/?inSys=wgsGeog&lat=22.2580467&long=114.00876443
    expected = {
        "hkN": 813259.701,
        "hkE": 818940.161,
    }

    ACCEPTED_TOLERANCE = 0.01
    assert abs(converted.easting - expected["hkE"]) <= ACCEPTED_TOLERANCE
    assert abs(converted.northing - expected["hkN"]) <= ACCEPTED_TOLERANCE
