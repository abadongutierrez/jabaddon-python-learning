import numpy as np 

a = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print("Full array:", a)
print("First 4 elements:", a[:4])
print("Elements from index 4:", a[4:])
print("Shape of array:", a.shape)
print("Data type of array:", a.dtype)

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)
print("Array A:\n", A)
print("Number of dimensions:", A.ndim)
print("Shape of array:", A.shape)
print("Total number of elements:", A.size)

print("Element at (1, 2):", A[1, 2])
print("Element at (1, 2) using [row][col] notation:", A[1][2])
print("Elements from row 0, columns 0 to 2:", A[0][0:2])

X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]])
print("Array X:\n", X)
print("Array Y:\n", Y)
Z = X + Y
print("Array Z (X + Y):\n", Z)
Z = X * 2
print("Array Z (X * 2):\n", Z)
Z = X @ Y
print("Array Z (X @ Y):\n", Z)
Z = X * Y
print("Element-wise multiplication (X * Y):\n", Z)
Z = np.dot(X, Y)
print("Dot product (X . Y):\n", Z)