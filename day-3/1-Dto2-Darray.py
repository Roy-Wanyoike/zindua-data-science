# converting from one dimension array to two-dimension array.

import numpy as np
x = np.array([x for x in range(9)])
final = x.reshape((3,3))
print(final)

