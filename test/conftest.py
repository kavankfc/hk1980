import pytest


@pytest.fixture
def valid_wgs84_point():
    latitude = 22.2580467
    longitude = 114.00876443
    return (latitude, longitude)  # NOTE: same location as valid_hk80_point


@pytest.fixture
def valid_hk80_point():
    northing = 813259.700
    easting = 818940.160
    return (northing, easting)  # NOTE: same location as valid_wgs84_point


@pytest.fixture
def invalid_wgs84_point():
    return (122.302711, 1114.177216)


@pytest.fixture
def invalid_hk80_point():
    return (1793259.700, 1848940.160)


@pytest.fixture
def min_hk80_point():
    return (799500, 799000)


@pytest.fixture
def max_hk80_point():
    return (867500, 848000)


@pytest.fixture
def min_wgs84_point():
    return (22.074428895, 113.491375844)


@pytest.fixture
def max_wgs84_point():
    return (22.341764663, 114.285001156)
