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

    # accepted tolerance is 0.00000001
    assert abs(converted.latitude - valid_wgs84_point[0]) <= 0.00000001
    assert abs(converted.longitude - valid_wgs84_point[1]) <= 0.00000001


def test_correct_conversion_to_hk1980(valid_wgs84_point, valid_hk80_point):
    converted = LatLon(*valid_wgs84_point).to_hk80()

    # accepted tolerance is 0.001
    assert abs(converted.easting - valid_hk80_point[0]) <= 0.001
    assert abs(converted.northing - valid_hk80_point[1]) <= 0.001
