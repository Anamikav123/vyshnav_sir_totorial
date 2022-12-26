def fun():
    a=10
    b=10
    c=a+b
    print(c)
fun()
print("----------------------------------")
def funn(a,b):
    c=a+b
    print(c)
funn(10,30)
print("----------------------------------")
def funnc(a,b):
    c=a+b
    return c
res=funnc(10,30)
t=100
print(res+t)
print("----------------------------------")
#positional argument
#Arbitary arguments
def ar(a,*b):
    print(a)
    print(b)
ar(10,20,44,99)
print("----------------------------------")
#keyword arguments
def ab(a,b,c):
    print(a)
    print(b)
    print(c)
ab(c=54,b=5,a=6)
print("----------------------------------")
#arbitary keyword argument
def abt(a,**b):
    print(a)
    print(b)
   
abt(c=54,b=5,a=6)
# default parameter
print("----------------------------------")
def defau(a,b=88):
    print(a)
    print(b)
defau(10)
print("----------------------------------")
def defau(a,b=88):
    print(a)
    print(b)
defau(10,55)