def factorial(x):
    if x==1:
        print(x)
        return x
    else:
        print(x)
        return x*factorial(x-1)
    #T(n)=T(n-1)+5 => O(n)

def for_factorial(x):  #O(n)   
    product=1
    for i in range(2,x+1):
        product*=i
    return product
