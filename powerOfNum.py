

def powerLinear(x,n): #O(n)
    product=1
    i=0
    while i<n:
        product=product*x
        i+=1
    return product


def powerLog(x,n): #O(logn)
    if n==0:
        return 1
    elif n==1:
        return x
    temp=powerLog(x,int(n/2))
    if n%2 ==0:
        return temp*temp
    else:
        return x*temp*temp
    #T(n)=9+T(n/2)

x=int(input("number: "))
p=int(input("power: "))
print(f"linear power result: {powerLinear(x,p)}")
print(f"logarithmic power result: {powerLog(x,p)}")
