class Solution:
    def firstMissingPositive(self, nums):
        nums_len = len(nums)
        for i in range(nums_len):
             while nums[i] > 0 and nums[i] <= nums_len\
                        and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
        print(nums)
        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1
        
        return nums_len + 1

if __name__ == "__main__":
    solution=Solution()
    nums=[3,4,-1,1]
    res=solution.firstMissingPositive(nums)
    print(res)