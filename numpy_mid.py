import numpy as np

arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([7,8,9,10,11,12])

print(np.vstack((arr2,arr1)))       #first array will be first row

print(np.vstack((arr1,arr2)))


print(np.hstack((arr1,arr2)))       #it will arrange to a single line

print(np.hstack((arr2,arr1)))

print(np.concatenate([arr1,arr2]))