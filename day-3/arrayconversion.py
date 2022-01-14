# this project was meant to check on how one can convert arrays
# it checks on converting from 1-D array to 3-D array

import numpy as np

a = np.array([x for x in range(27)])

o = a.reshape((3,3,3))

print(o)