import numpy as np

#### Creating Arrays from Python list ####

# Creating array 
a = np.array([1, 2, 3, 6, 10])
b = np.array([1, 2, 3, 6, 10], dtype="float32")

# Nested list results in multidimensional arrays
c = np.array([range(i, i+2) for i in a])

#### Creating Arrays from Scratch ####

# Create a length -10 integer array filled with zeros
zeros = np.zeros(10, dtype="int")
print(zeros)

# Create a 3x5 floating-point array filled with 1s
ones = np.ones(shape=(3, 5), dtype="int")
print(ones)

# Create a 3x5 array filled with 3.14
fulls = np.full(shape=(3, 5), fill_value=3.14, dtype="float")
print(fulls)

# Create an array filled with a linear sequence
in_range = np.arange(2, 22, 4)
print(in_range)

# Create a 3x3 array of uniformly distributed random values between 0 and 1
uni_random = np.random.random((3, 3))
print(uni_random)

# Create a 3x3 array of normally distributed with mean 0 and standard deviation 1
normal_random = np.random.normal(loc=0, scale=1, size=(3, 3))
print(normal_random)

# Create a 3x3 array of random integers in the interval [0, 10)
interval_random = np.random.randint(low=0, high=10, size=(3, 3), dtype="int")
print(interval_random)

# Create 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# Create an uninitialiezed array of the three integers
empty_matrix = np.empty(3)
print(empty_matrix)

#### The Basics of Numpy Arrays ####

# Numpy Array Attributes
np.random.seed(123)

x1 = np.random.randint(0, 10, size=3)
x2 = np.random.randint(0, 10, size=(3, 4))
x3 = np.random.randint(0, 10, size=(3, 4, 5))

print("x1 ndim:", x1.ndim)
print("x2 shape:", x2.shape)
print("x3 size:", x3.size)
print("x1 dtype:", x1.dtype)
print("x2 itemsize:", x2.itemsize, "bytes")
print("x3 bytes:", x3.nbytes, "bytes") 

# Array Indexing: Accessing Single Elements

print(x1) # whole array vector
print(x1[0]) # first array observation
print(x1[2]) # third array observation 
print(x1[-1]) # first in back array observation
print(x1[-2]) # second in back array observation
print(x2) # whole array twodimensional matrix 
print(x2[0, 0]) # 1x1 matrix observation 
print(x2[2, 2]) # 3x3 matrix observation
print(x2[2, -1]) # 3x-1 matrix observation (3x4)

x = np.arange(10)

print(x) # whole array vector
print(x[:5]) # observation from index 1 to 5
print(x[5:]) #observation from index 6 to 10
print(x[4:7]) # middle elements
print(x[::2]) # every other element
print(x[1::2]) # every other element, starting at index 1
print(x[::-1]) # all elements reversed
print(x[5::-2]) #reversed every other form index 5
      
