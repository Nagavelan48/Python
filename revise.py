# s = set()
# n = int(input("Enter the number"))
# for i in range(n):
#     val = int(input("The elements are"))
#     s.add(val)
# print(s)

# s = {1,2,3,4,5,6,1,1,3,4,6}
# print(s)

# d = {}
# n =int(input("Enter the number"))
# for i in range(n):
#     key = int(input("Enter the keys"))
#     value = input("Enter the value")
#     d[key]=value

# print(d)
# def list1(n,l):
#     for i in range(n):
#         val = input("Enter the value")
#         l.append(val)

# l = []
# n = int(input("Enter the number"))

# list1(n,l)
# print(l)


arr = [1,2,3,4,5,6,7,8]
val = list(filter(lambda x:x%2==1,arr))
print(val)