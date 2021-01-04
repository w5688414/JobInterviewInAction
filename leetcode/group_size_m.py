class Solution:
    def findLatestStep(self, arr, m: int):
        if(len(arr)==m):
            return m
        res=-1
        border=[0]*(len(arr)+2)
        for i,num in enumerate(arr):
            l=r=num
            if(border[r+1]>0):
                r=border[r+1]
            if(border[l-1]>0):
                l=border[l-1]
            border[l]=r
            border[r]=l
            if(r-num==m or num-l==m):
                res=i
            print(border)
        # print(border)
        return res
        
if __name__ == "__main__":
    solution=Solution()
    arr = [3,5,1,2,4]
    m = 2
    res=solution.findLatestStep(arr,m)
    print(res)
