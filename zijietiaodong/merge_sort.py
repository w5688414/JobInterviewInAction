
class Solution():
    def __init__(self):
        super().__init__()
    
    def merge(self,arr1,arr2):
        i,j=0,0
        m=len(arr1)
        n=len(arr2)
        res=[]
        while(i<m and j<n):
            if(arr1[i]<=arr2[j]):
                res.append(arr1[i])
                i+=1
            else:
                res.append(arr2[j])
                j+=1
        for p in range(i,m):
            res.append(arr1[p])
        for p in range(j,n):
            res.append(arr2[p])
        return res

    def merge_list(self,arr):
        if(len(arr)<=1):
            return arr
        n=len(arr)
        middle=n//2
        left=self.merge_list(arr[:middle])
        right=self.merge_list(arr[middle:])
        return self.merge(left,right)

if __name__ == "__main__":
    solution=Solution()
    arr=[1,2,10,4,1,4,3,3]
    res=solution.merge_list(arr)
    print(res)