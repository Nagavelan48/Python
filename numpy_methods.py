import numpy as np

arr = np.array([[1,2,3,4,5,6],[7,8,9,0,1,2]])

# print(arr.shape)
# print(arr.dtype)

# print(np.zeros((2,3)))   #used to create zero matrix

# print(np.eye(4))        #used to create the identity mmatrix

# print(arr[0])
# print(arr[1:4])
# print(arr[::-1])
# print(arr[1,2])
# print(arr[:,1])

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(arr.flatten())        #modify into single array
print(arr.reshape(3,4))      #modify the array