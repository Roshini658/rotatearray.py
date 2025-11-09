arr=[1,2,3,4]
def reverseArr(arr,l,r):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
def rotateArr(arr,d):
    n=len(arr)
    d=d%n
    reverseArr(arr,0,d-1)
    reverseArr(arr,d,n-1)
    reverseArr(arr,0,n-1)
rotateArr(arr,9)
print(arr)