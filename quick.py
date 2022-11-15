def quick(list):
    if len(list)<=1:
        return list
    left=[]
    right =[]
    pivot=list[0]
    for i in list[1:]:
        if i<= pivot:
            left.append(i)
        else:
            right.append(i)
    print(left, pivot, right)
    return quick(left) + [pivot] + quick(right)
