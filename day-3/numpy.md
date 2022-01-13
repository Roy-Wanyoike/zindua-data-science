
`**What is Numpy and getting started**`
Numpy is a python library which is used to provide mathematical solutions. 
It is a short form for **numerical python *(NumPy)***.
It provides the functionality to work with multidimensional array of objects, assortment of routines for quick array operations alongside other derived objects. 
Fast array operations in arrays include:
- mathematics
- logical
- shape manipulation
- sorting
- selection
- I/O
- discrete Fourier transforms
- basic linear algebra
- basic statistical operations
- random simulation etc


**How to install numpy**
it comes with python in most scenario and has only to be imported. However, it requires the installation of anaconda library for easy functioning. 
to install conda run the following

`conda install numpy`


To use pip to install run the following on the commandline:


`pip install numpy`


Numpy doesn't depend on any python package  but only the accelerated linear algebra library. These are  intel KL and OpenBLAS. The advantage is that they come preinstalled in python. BLAS has some effects on performance and behavior hence if interested one can check on them. 
Numpy API is used in pandas, Scipy, Matplotlib, sckikit-learn, scikit-image and other data science python packages. 
Numpy library is composed of the multidimensional array and matrix data structures. 
It is inside where there is the ndarray which is a homogenous n-dimensional array object. You understand when i mean n-dimension meaning the number is large not constant or definite. 

we checked on how to install the numpy.
For pip users run

`pip  install numpy`

for conda users run:

`conda install numpy`

*Working with numpy*

To use  numpy in your code start by importing the numpy library.
 
` import numpy as np`

the reason for using np is to increase readability and reducing lot of large words in the code. 
To use it simply use np anywhere when calling it. 
It is a common convetion used by many hence easy for anyone to understand your code.

# _example of code_

`import numpy as np`

`>>> a = np.arrange(6)`

`>>> a2 = a[np.newaxis, :]`

`>>> a2.shape `

`(1,6)`

for the above code the forward arrows shows a user input while the latter one with no pointers shows the output.

# **Difference between python list and numpy array**

- numpy has several enormous range of fast and efficient ways of creating arrays.
It also provides ways to manipulate the numerical data inside them. 
- On the other hand python list contains different data types within a single list.
- This means the data type in python are heterogenous(different data types) while for NumPy are homogenous(same data type)