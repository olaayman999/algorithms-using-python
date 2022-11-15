
#f(n)= f(n-1)+f(n-2) as n>1
#      n as n=1 or n=0
#0 1 1 2 3 5 8....

global memory
memory =[]
memory.append(0)
memory.append(1)
memory.append(1)

import sys
print(f"your max index limit is {sys.getrecursionlimit()}")

'''
        !!!maximum recursion depth exceeded in comparison error!!!
It is a guard against a stack overflow, the depth limit can be changed using

                sys.setrecursionlimit(1500)

but doing so is dangerous -- the standard limit is a little conservative, but Python stackframes can be quite big. Python isn't a functional language and tail recursion is not a particularly efficient technique. Rewriting the algorithm iteratively, if possible, is generally a better idea.
'''
for i in range(3,1000):
    memory.append(-1)
    
def feb(n):                                     
    if n<=1:
        return n
    else:
        return feb(n-1)+feb(n-2)
#T(n)=T(n-1)+T(n-2)+3 O(2^n) space copmlexity =1
#use this in case of n [0 to 30]
'''     
               f5
           /        \
        f4           f3
        /\          /  \ 
      f3  f2       f2   f1  
     / \  / \     / \   
    f2 f1 f1 f0  f1 f0 
   / \
 f1  f0
 
 recurtion is not always the best solution
'''
def FebWithMemory(n):
    if memory[n] != -1:
        #print(f"found number at index {n}")
        return memory[n]
    else:
        memory[n]=FebWithMemory(n-1)+FebWithMemory(n-2)
        return memory[n]
    #space complexty =n
    
    '''  
    Assume T(n) is the time complexity of n, so T(n) = T(n-1) + T(n-2). Because F(n-2) is in the cache when we calculate F(n - 1), so the operation of F(n-2) is 1(reading from cache), so T(n) = T(n-1) + 1 = T(n-2) + 2 = ... = T(n-n) + n. And T(0) is 1, so T(n) = O(n + 1) = O(n).
               f5
           /      \
        f4         f3
        /\          
      f3  f2        
     / \             
    f2 f1        
   / \
 f1  f0
 
 reducing redundunt calls
'''
    
x=int(input("number: "))
#print(feb(x))
str=str(FebWithMemory(x))
print(f"the number at index {x} is {str}")
print(f"which is {len(str)} digits long !!")
