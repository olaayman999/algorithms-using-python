#strings are noy mutable so we need the pocket to store the swapped letters
# string -> the string of letters that we want to swap
#pocket -> new swapped string
def permute(string, pocket=""): 
    if len(string)==0:
        print(pocket) 
    else:
        for i in range(len(string)):
            letter=string[i]  
            head=string[0:i] 
            tail=string[i+1:] 
            together=head+tail 
            print(f"string: {string} letter: {letter} head: {head} tail: {tail} pocket: {pocket}")
            permute(together, letter + pocket)
            

from itertools import permutations
x=input("type your string: ")
l=list(permutations(x))
print(l)