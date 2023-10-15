
##1. Create a null vector of size 10 but the fifth value which is 1.

# import numpy as np
# Z = np.zeros(10)
# Z[4] = 1
# print(Z)

##2. Create a vector with values ranging from 10 to 49.

# import numpy as np
# Z = np.arange(10,50)
# print(Z)

##3. Create a 3x3 matrix with values ranging from 0 to 8

# import numpy as np
# Z = np.arange(9).reshape(3, 3)
# print(Z)

##4. Find indices of non-zero elements from [1,2,0,0,4,0]

# import numpy as np
# nz = np.nonzero([1,2,0,0,4,0])
# print(nz)

##5. Create a 10x10 array with random values and find the minimum and maximum values.

# import numpy as np
# Z = np.random.random((10,10))
# Zmin, Zmax = Z.min(), Z.max()
# print(Zmin, Zmax)

##6. Create a random vector of size 30 and find the mean value.

# import numpy as np
# Z = np.random.random(30)
# m = Z.mean()
# print(m)