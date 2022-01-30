# hk1980
A forked project from hk80. This project also convert the coordinates between Hong Kong 1980 Grid System and World Geodetic System 1984 with pyproj, with a more update version of `pyproj` and providing better performance. 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) or [poetry](https://python-poetry.org/) to install foobar.

```bash
pip install hk1980
```
or
```bash
poetry add hk1980
```

## Usage

```python
from hk1980 import LatLon, HK80

hku = LatLon(22.284034, 114.137814).to_hk80()
print(hku.northing, hku.easting) # 836303.204 818195.94
print(hku.x, hku.y) # 818195.94 836303.204

hku = HK80(northing=816128, easting=832243).to_wgs84()
print(hku.latitude, hku.longitude) # 22.42944514 113.98124272
print(hku.x, hku.y) # 113.98124272 22.42944514
```
## Performance

hk1980 is roughly well performant than hk80 than 238 times.

```python
#hk80
import timeit
stmt = "LatLon(22.284034, 114.137814).to_hk80()"
_time_ms = timeit.timeit(stmt=stmt, globals=globals(), number=100)*1000
print(f"time: {_time_ms} ms") # 238.1038 ms

#hk1980
import timeit
stmt = "LatLon(22.284034, 114.137814).to_hk80()"
_time_ms = timeit.timeit(stmt=stmt, globals=globals(), number=100)*1000
print(f"time: {_time_ms} ms") # 1.0652 ms
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)