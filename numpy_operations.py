import numpy as np

# a=np.array([1,2,3,4])
# b=np.array([[1,2,4,5],[4,5,7,8]])
# print(a)
# print(b)
# print(a.shape)
# print(b.shape)

# print(a.dtype)

a = []
n =int(input("Enter the number"))
for i in range(n):
    val = int(input("Values"))
    a.append(val)

arr=np.array(a)
print(arr)