
def partition(arr,l,h):
    key=arr[l]
    i=l
    j=h
    while(i<j):
        while(i<j and key<=arr[j]):
            j-=1
        arr[i]=arr[j]
        while(i<j and key>=arr[i]):
            i+=1
        arr[j]=arr[i]
    arr[i]=key
    return i

def quick_sort(arr,l,h):
    if(l<h):
        mid=partition(arr,l,h)
        quick_sort(arr,l,mid-1)
        quick_sort(arr,mid+1,h)
    return arr


if __name__ == "__main__":
    arr=[1,2,10,4,1,4,3,3]
    n=len(arr)
    res=quick_sort(arr,0,n-1)
    print(res)