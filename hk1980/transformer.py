from pyproj import CRS, Transformer

COORD_WGS1984 = CRS("EPSG:4326")
COORD_HK1980 = CRS("EPSG:2326")

TRANSFORMER_WGS1984_TO_HK1980 = Transformer.from_crs(COORD_WGS1984, COORD_HK1980)
TRANSFORMER_HK1980_TO_WGS1984 = Transformer.from_crs(COORD_HK1980, COORD_WGS1984)