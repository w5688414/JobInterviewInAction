class Solution:
    def minSubarray(self, nums, p):
        target=sum(nums)%p
        if(target==0):
            return 0
        d={0:-1}
        n=len(nums)
        cur=0
        res=n
        print(target)
        list_data=[]
        list_arr1=[]
        for i in range(n):
            cur=(cur+nums[i])%p
            # print(cur)
            # print(cur-target)
            list_data.append(cur)
            if(d.get((cur-target)%p) is not None):
                res=min(res,i-d.get((cur-target)%p))
                list_arr1.append((cur-target)%p)
                # print((cur-target)%p)
                # print(res)
            d[cur]=i
        print(d)
        print(list_data)
        print(list_arr1)
        if(res<n):
            return res
        return -1

if __name__ == "__main__":
    nums = [3,1,4,2]
    p = 6
    solution=Solution()
    res=solution.minSubarray(nums,p)
    print(res)