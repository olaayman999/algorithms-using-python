def selection(list): 
    sorted =[]
    size=len(list)
    while len(list) >0:
        min=99999999999999999
        j=0
        while j < len(list):
            if  list[j]<=min:
                min=list[j]
                index_min=j
            j+=1
        list.pop(index_min)
        sorted.append(min)
    
    print(verify(sorted, size))
    return(sorted)

def verify(list, size):
    if (len(list) != size):
        return False
    else:
        if len(list)<=1:
            return True
        return list[0]<=list[1] and verify(list[1:], size-1)