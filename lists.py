# set1=set([1,2,3,4,4,3,6,7,2,5,3])
# print(set1)
# set2={4,5,6,7,8}
# print(set1.union(set2))
# print(set1.pop())
# print(set1)
# print(set1.add(7))
# print(set1)
# n=int(input("Enter the length"))
# set1=set()
# for i in range(n):
#     num=int(input("Enter the element"))
#     set1.add(num)

# print(set1)

s={}
n=int(input("Enter the length"))
for i in range(n):
    num=int(input("Enter the key"))
    value=input("Enter the value")
    s[num]=value
print(s)
print(s.keys())
print(s.values())
