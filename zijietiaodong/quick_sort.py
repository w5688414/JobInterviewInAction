class Solution():
    def __init__(self):
        super().__init__()
    
    def partition(self,arr,low,high):
        key=arr[low]
        while(low<high):
            while(low<high and key<=arr[high]):
                high-=1
            arr[low]=arr[high]
            while(low<high and key>=arr[low]):
                low+=1
            arr[high]=arr[low]
            arr[low]=key
        return low
    def quick_sort(self,arr,low,high):
        if(low<high):
            p=self.partition(arr,low,high)
            self.quick_sort(arr,low,p-1)
            self.quick_sort(arr,p+1,high)
        return arr

    def solve(self,arr):
        low=0
        high=len(arr)-1
        res=self.quick_sort(arr,low,high)
        print(res)

if __name__ == "__main__":
    # arr=[0,1,2,1]
    arr=[1, 1, 2, 4, 10, 4, 3, 3]
    solution=Solution()
    solution.solve(arr)
 
