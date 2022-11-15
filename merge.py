import linked_list

def merge_sort(list):
    
    #the stopping condition of the recursive fuction, single element list or empty list, this is called naiive sorting
    if len(list)<=1:
        return list
    
    #splitting the list and this global fuction will return 2 variables so we'll catch them in 2 vars
    left_half,right_half=split(list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    
    return merge(left, right)


def split(list): #O(K logn)
    
    #floor division that returns only int
    mid=len(list)//2
    left=list[:mid] #from start to mid but not including mid
    right=list[mid:]
    
    return left, right


def merge(left, right): #O(Kn logn)
    
    #the function will return new merged and sorted list
    l=[]
    #index i and j keep track of left and right list
    i=0; j=0;
    
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    
    while i<len(left):
        l.append(left[i])
        i+=1
        
    while j<len(right):
        l.append(right[j])
        j+=1
        
    return l
    

def verify(list):
    n=len(list)
    if n<=1:
        return True
    return list[0]<=list[1] and verify(list[1:])