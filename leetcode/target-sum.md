# problem
>You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
```
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
```
Note:
- The length of the given array is positive and will not exceed 20.
- The sum of elements in the given array will not exceed 1000.
- Your output answer is guaranteed to be fitted in a 32-bit integer.

# codes
```
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
        int sum=accumulate(nums.begin(),nums.end(),0);
        return sum<S||(S+sum) & 1 ? 0:subsetSum(nums,(sum+S)>>1);
    }
    int subsetSum(vector<int>& nums,int s ){
        int dp[s+1]={0};
        dp[0]=1; // 初始记录0的位置为1
        for(int n:nums){
            // 对每个元素，看看他现有能和别的元素相加得到哪些位置的数
            for(int i=s;i>=n;i--){
                dp[i]+=dp[i-n];
            }
        }
        return dp[s];
    }
};
```

# analysis
>动态规划的题目，不会，明天再看。
```
sum(P) - sum(N) = target  
sum(P) - sum(N) = target + sum(P) + sum(N)  
     2 * sum(P) = target + sum(nums) 
```
nums = {1,2,3,4,5}, target=3
- 求解nums中子集合只和为sum(P)的方案个数(nums中所有元素都是非负)
给定集合nums={1,2,3,4,5}, 求解子集，使子集中元素之和等于9 = new_target = sum(P) = (target+sum(nums))/2
当前元素等于1时，dp[9] = dp[9] + dp[9-1]
            dp[8] = dp[8] + dp[8-1]
            ...
            dp[1] = dp[1] + dp[1-1]
当前元素等于2时，dp[9] = dp[9] + dp[9-2]
            dp[8] = dp[8] + dp[8-2]
            ...
            dp[2] = dp[2] + dp[2-2]
当前元素等于3时，dp[9] = dp[9] + dp[9-3]
            dp[8] = dp[8] + dp[8-3]
            ...
            dp[3] = dp[3] + dp[3-3]
当前元素等于4时，
            ...
当前元素等于5时，
            ...
            dp[5] = dp[5] + dp[5-5]
最后返回dp[9]即是所求的解

# reference
[494. Target Sum][1]
[leetcode -- 494. Target Sum【数学转化 + 动态规划】][2]
[494. Target Sum][3]

[1]: https://leetcode.com/problems/target-sum/discuss/97334/Java-(15-ms)-C++-(3-ms)-O(ns)-iterative-DP-solution-using-subset-sum-with-explanation
[2]: https://blog.csdn.net/thesnowboy_2/article/details/55095053
[3]: https://blog.csdn.net/hit0803107/article/details/54894227

