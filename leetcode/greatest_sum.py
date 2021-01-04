class Solution:
    def maxSumDivThree(self, nums):
        n=len(nums)
        dp=[0]*(3)
        for num in nums:
            dp1=[item for item in dp]
            for s in dp1:
                dp[(s+num)%3]=max(dp[(s+num)%3],s+num)
            print(dp)
        return dp[0]



if __name__ == "__main__":
    nums = [3,6,5,1,8]
    solution=Solution()
    res=solution.maxSumDivThree(nums)
    print(res)
