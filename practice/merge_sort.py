
def merge(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    i=0
    j=0
    res=[]
    while(i<m and j<n):
        if(arr1[i]<=arr2[j]):
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    while(i<m):
        res.append(arr1[i])
        i+=1
    while(j<m):
        res.append(arr2[j])
        j+=1
    return res

def merge_sort(arr):
    if(len(arr)==1):
        return arr
    n=len(arr)
    mid=n//2
    arr1=merge_sort(arr[:mid])
    arr2=merge_sort(arr[mid:])
    return merge(arr1,arr2)

if __name__ == "__main__":
    arr=[1,2,10,4,1,4,3,3]
    res=merge_sort(arr)
    print(res)