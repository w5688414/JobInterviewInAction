
class Solution():
    def __init__(self):
        super().__init__()

    def adjust(self,arr,n,i):
        largest=i
        l=2*i+1
        r=2*i+2
        if(l<n and arr[largest]<arr[l]):
            largest=l
        if(r<n and arr[largest]<arr[r]):
            largest=r
        if(i!=largest):
            arr[largest],arr[i]=arr[i],arr[largest]
            self.adjust(arr,n,largest)
    def solve(self,arr):
        n=len(arr)
        for i in range(n//2-1,-1,-1):
            self.adjust(arr,n,i)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.adjust(arr,i,0)
        return arr
if __name__ == "__main__":
    solution=Solution()
    # arr=[5,3,7,9,2,3,7]
    # arr= [1,2,10,4,1,4,3,3]
    arr= [5, 6, 4, 2, 3,1,2]
    res=solution.solve(arr)
    print(res)
