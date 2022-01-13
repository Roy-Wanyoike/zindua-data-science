Basics of Numpy

-As we said earlier numpy is a shortform for numerical python. 
This topic will cover some basics of numpy ranging from:
- Numpy attributes
- Array indexing
- Array slicing
- Reshaping arrays
- Joining arrays
- Splitting arrays'

  **_NUMPY ARRAY ATTRIBUTES_**
- This helps in determining the shape, size, memory consumption and also the data types of arrays.In this topic we will check on the types of array;-
- one-dimension array
- two-dimension array
- three-dimensional array

**1. the ndim attribute**
we can check the number of dimensions using ndim(number of dimensions) and the size(total size of the array)

`import numpy as np
np.random.seed(0) #seed for reproducibility
x1 = np.random.randint(10, size=(3,4))
#produces a one dimension array
x2 = np.random.randint(10, size=(3,4))
#produces a two dimension array
x3 = np.random.randint(10, size=(3,4,5))
#produces a three dimension array`

To see output we can print the following;

`print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size:", x3.size)
` 

 **2. The dtype attribute**
 
- This attribute checks on the type of data present. 
- It shows the type of data if its integer, float, string or any other data type.
 -It takes place by simply typing dtype after the data.

   `print("dtype:", x3.dtype")`

  output
       `dtype: int64`
