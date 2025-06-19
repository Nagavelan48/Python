arr = [1,2,3,4,5]
it = iter(arr)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))

def check(x):
    while(x>0):
        if(x%2==0):
            yield x
            x=x-2
        x=x-7  

for i in check(100):
    print(i)