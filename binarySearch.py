

def binarySearch(arr,left,right,key):
    middle=int(left+(right-left)/2)
    print(f"pivot is index {middle} where value is {arr[middle]}")
    print(f"current search on: {arr[left:right+1]}")
    if(key>arr[-1] or key<arr[0]):
        return -1
    elif(key==arr[middle]):
        return middle
    elif(key>arr[middle]):
        return binarySearch(arr,middle+1,right,key)
    else:
        return binarySearch(arr, left, middle-1, key)
    

arr=[]
n=int(input("enter number of elements: "))
#this is how to take a list as an input
for i in range(n):
    element=int(input(f"enter element number {i+1}: "))
    arr.append(element)
#to use binary search algorithm the list needs to be sorted
arr.sort()
x=int(input("enter your key: "))
print(binarySearch(arr,0,len(arr)-1,x))