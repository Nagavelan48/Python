from functools import reduce


def greet(name="Buddy"):
    print( f"Hello , {name}")

greet()
greet("Velan")


def detail(age,name):
    print(f"This person age is {age} and name is {name}")
detail(name="Velan",age=22)

def check(x):
    if isinstance(x, int) and x > 8:
        return x

def add(*args,**kwargs):
    num=list(map(lambda x: x*x,args))
    print(num)
    res=list(filter(check,kwargs.values()))
    print(res)

add(2,3,5,6,num=6,num1=8,num2=9,num3=12)