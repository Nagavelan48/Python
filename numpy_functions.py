import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
arr2 = np.array([9,10,11,12,13,14,15,16])
b =  100
mat = np.array([[1,2,3],[4,5,6],[7,8,0]])
# print(arr[arr>6])
print(arr2*2)
# print(arr[arr%3==0])

# print(arr*b)

# print(np.random.rand(3))

# print(np.random.randint(2,9,6))

# print(np.random.randint(1,20,(2,4)))


# str = ["a","b","c","d"]
# print(np.random.choice(str))
# print(np.dot(arr,arr2))
# print(np.linalg.inv(mat))
# print(np.linalg.det(mat)  ) 
# print(np.linalg.eig(mat) )


np.save('sample_save.npy',mat)
np.savetxt('sample_save.csv',mat)
print(np.loadtxt('sample_save.csv'))