
def adjust(arr,n,i):
    l=2*i+1
    h=2*i+2
    largest=i
    if(l<n and arr[largest]<arr[l]):
        largest=l
    if(h<n and arr[largest]<arr[h]):
        largest=h
    if(i==largest):
        return 
    else:
        arr[i],arr[largest]=arr[largest],arr[i]
        adjust(arr,n,largest)

def heap_sort(arr):
    n=len(arr)
    for i in range(n//2,-1,-1):
        adjust(arr,n,i)
    for i in range(n-1,-1,-1):
        arr[i],arr[0]=arr[0],arr[i]
        adjust(arr,i,0)
    return arr
    
if __name__ == "__main__":
    arr=[1, 1, 2, 4, 10, 4, 3, 3]
    res=heap_sort(arr)
    print(arr)