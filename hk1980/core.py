import warnings
from typing import Literal

from hk1980.transformer import (
    TRANSFORMER_HK1980_TO_WGS1984,
    TRANSFORMER_WGS1984_TO_HK1980,
)


class Point:
    def __init__(
        self,
        x: float,
        y: float,
        x_min: float,
        y_min: float,
        x_max: float,
        y_max: float,
        on_error: Literal["raise", "warning", "coerce"] = "raise",
    ):
        """An abstract class of point and do the validation at init stage.

        Args:
            x (float): Horizontal point location.
            y (float): Vertical point location.
            x_min (float): Minimum horizontal point location.
            y_min (float): Minimum vertical point location.
            x_max (float): Maximum horizontal point location.
            y_max (float): Maximum vertical point location.
            on_error (Literal[, optional): Error handling approach. Defaults to "raise".
        """
        if on_error not in ["raise", "warning", "coerce"]:
            raise ValueError("on_error only accept 'raise', 'warning', or 'coerce'")
        self.on_error = on_error

        self._error_check = False
        if self.on_error == "raise":
            self._error_check = True

        self.x_min, self.x_max = x_min, x_max
        if not (self.x_min <= x <= self.x_max) and self.on_error == "warning":
            warnings.warn("invalid x coordinate passed", UserWarning)

        self.y_min, self.y_max = y_min, y_max
        if not (self.y_min <= y <= self.y_max) and self.on_error == "warning":
            warnings.warn("invalid y coordinate passed", UserWarning)

        self.x, self.y = x, y


class LatLon(Point):
    def __init__(self, latitude: float, longitude: float, on_error: str = "raise"):
        """Contruct a LatLon Object, bounded in hk, according to the boundary of hk1980 calculated in https://www.geodetic.gov.hk/en/services/tform/tform.aspx

        Args:
            latitude (float): WGS 84 latitude in decimal degrees, scale: 8 .
            longitude (float): WGS 84 longitude in decimal degrees, scale: 8.
            on_error (str, optional): Error handling approach. Defaults to "raise".
        """
        latitude = round(latitude, 8)
        longitude = round(longitude, 8)
        super().__init__(
            x=longitude,
            y=latitude,
            x_min=113.491375844,
            y_min=22.074428895,
            x_max=114.285001156,
            y_max=22.341764663,
            on_error=on_error,
        )

    @property
    def longitude(self):
        return self.x

    @property
    def latitude(self):
        return self.y

    def __str__(self):
        return f"LatLon(latitude={self.latitude}, longitude={self.longitude})"

    def to_hk80(self) -> Point:
        return HK80(
            *TRANSFORMER_WGS1984_TO_HK1980.transform(
                self.y, self.x, errcheck=self._error_check
            )
        )


class HK80(Point):
    def __init__(self, easting: float, northing: float, on_error: str = "raise"):
        """Contruct a HK80 Object, bounded in hk

        Args:
            easting (float): Hong Kong 1980 Grid system easting (x) in meters, scale: 3.
            northing (float): Hong Kong 1980 Grid system northing (y) in meters, scale: 3.
            on_error (str, optional): Error handling approach. Defaults to "raise".
        """

        easting = round(easting, 3)
        northing = round(northing, 3)

        """
        super().__init__(
            x=easting,
            y=northing,
            x_min=793259.700,
            y_min=799130.010,
            x_max=870525.780,
            y_max=848940.160,
            on_error=on_error,
        )
        """
        # boundary are set according to https://www.geodetic.gov.hk/transform/tformAPI_manual.pdf
        super().__init__(
            x=easting,
            y=northing,
            x_min=799500,
            y_min=799000,
            x_max=867500,
            y_max=848000,
            on_error=on_error,
        )

    @property
    def easting(self):
        return self.x

    @property
    def northing(self):
        return self.y

    def __str__(self):
        return f"HK80(northing={self.northing}, easting={self.easting})"

    def to_wgs84(self) -> Point:
        return LatLon(
            *TRANSFORMER_HK1980_TO_WGS1984.transform(
                self.x, self.y, errcheck=self._error_check
            )
        )
