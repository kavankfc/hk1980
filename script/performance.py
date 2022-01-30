import cProfile
import timeit

from hk1980 import LatLon

stmt = "LatLon(22.284034, 114.137814).to_hk80()"

time = timeit.timeit(stmt=stmt, globals=globals(), number=100)*1000
print(f"{time=}  ms")

cProfile.run(stmt)