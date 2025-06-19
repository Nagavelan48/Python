from functools import reduce


s=lambda x:x/x
print(s(5))

arr = [1,2,3,4,5]
out = list(map(lambda x: x*x, arr))
print(out)


# def check(x):
#     if(x%2==0):
#         return x
#     else:
#         return 0
nums = [1,2,3,4,5,6,7,8,12]
output = list(filter(lambda x: x%2==0 , nums))
print(output)

z = [9,8,7,6,5,4]
res = reduce(lambda x,y : x+y , z)
print(res)
