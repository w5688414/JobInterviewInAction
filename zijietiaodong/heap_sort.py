
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

        if(largest!=i):
            arr[largest],arr[i]=arr[i],arr[largest]
            self.adjust(arr,n,largest)

    def solve(self,arr):
        n=len(arr)
        for i in range(n//2-1,-1,-1):
            self.adjust(arr,n,i)
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.adjust(arr,i,0)
        return arr

if __name__ == "__main__":
    solution=Solution()
    arr=[1,2,10,4,1,4,3,3]
    res=solution.solve(arr)
    print(res)
