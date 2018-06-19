# problem
>You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
```
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```
Example 2:
```
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

# codes
```
class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size()==0){
            return 0;
        }
        if(nums.size()==1){
            return nums[0];
        }
        return max(rob(nums,0,nums.size()-1),rob(nums,1,nums.size()));
    }
    int rob(vector<int> nums,int left,int right){
        if(right-left<=1){
            return nums[left];
        }
        vector<int> dp(right,0);
        dp[left]=nums[left];
        dp[left+1]=max(nums[left],nums[left+1]);
        for(int i=left+2;i<right;i++){
            dp[i]=max(dp[i-2]+nums[i],dp[i-1]);
        }
        return dp[right-1];
    }
};
```

# analysis
- 现在房子排成了一个圆圈，则如果抢了第一家，就不能抢最后一家，因为首尾相连了，所以第一家和最后一家只能抢其中的一家，或者都不抢，那我们这里变通一下，如果我们把第一家和最后一家分别去掉，各算一遍能抢的最大值，然后比较两个值取其中较大的一个即为所求。
dp[i]表示前i个房子，强盗能够抢到的最大值。

# reference
[[LeetCode] House Robber II 打家劫舍之二][1]

[1]: https://www.cnblogs.com/grandyang/p/4518674.html
