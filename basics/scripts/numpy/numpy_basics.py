import numpy as np 

a = np.array([0, 1, 2, 3, 4])
print(a)

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# check version
print(np.__version__)
print("Type: ", type(a))
print("Shape: ", a.shape)
print("Dimensions: ", a.ndim)
print("Size: ", a.size)
print("Data type: ", a.dtype)
print("Item size: ", a.itemsize)
print("Total bytes: ", a.nbytes)

# assigning a value
a[0] = 10
print("Updated a[0]:", a[0])

# slicing
print("Sliced a[1:4]:", a[1:4])

# set elements
a[1:4] = 22, 33, 44
print("Updated a[1:4]:", a[1:4])

print("Full array:", a)
print(a[:4])
print(a[4:])
print(a[1:4:]) # step
print(a[::2]) # every second element


b = np.array([10, 20, 30, 40, 50, 60, 70])
print("Array b:", b)
print("mean:", b.mean())
print("Standard Deviation:", b.std())
# max
print("Max:", b.max())
print("Min:", b.min())

#Addition
u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
print("Addition:", z)
# Subtraction
z = np.subtract(u, v)
print("Subtraction:", z)
# Multiplication
z = np.multiply(u, v)
print("Multiplication:", z)

a = np.array([10, 20, 30])
b = np.array([2, 10, 5])
c = np.divide(a, b)
print("Division:", c)
print("Data type:", c.dtype)

X = np.array([1, 2])
Y = np.array([3, 2])
Z = np.dot(X, Y)
# X.Y = [(X[0] * Y[0]) + (X[1] * Y[1])]
# X.Y = (1 * 3) + (2 * 2)
# X.Y = 3 + 4
# X.Y = 7
print("Dot product:", Z)

# Adding a constant
u = np.array([1, 2, 3, -1]) 
v = u + 3
print("Adding a constant:", v)

# Radians
x = np.array([0, np.pi/2 , np.pi])
y = np.sin(x)
print("Sine values:", y)

# import time 
# import sys
# import numpy as np 

# import matplotlib.pyplot as plt


# def Plotvec1(u, z, v):
    
#     ax = plt.axes() # to generate the full window axes
#     ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
#     ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
#     plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
#     ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
#     plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
#     plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
#     plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Plotvec1(u, z, v)

a=np.array([0,1,0,1,0]) 

b=np.array([1,0,1,0,1]) 

print(a*b)
