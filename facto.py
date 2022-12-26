n=int(input("enter a number:"))
fact=1
if n<0:
    print("no factorial for negative number")
else:
    for i in range(1,n+1):
        fact = fact*i#fact*=i
    print("The factorial of",n,"is",fact) 