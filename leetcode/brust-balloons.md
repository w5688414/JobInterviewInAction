# problem
>Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:
```
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
```

# codes
```
class Solution {
public:
    int maxCoins(vector<int>& nums) {
       vector<int> temp(nums.size()+2,0);
        int n=1;
        for(auto num:nums){
            if(num>0){
                temp[n]=num;
                n++;
            }
        }
        temp[0]=temp[n]=1;
        n++;
        int dp[n][n]={};
        for(int k=2;k<n;k++){
            for(int left=0;left<n-k;left++){
                int right=left+k;
                for(int i=left+1;i<right;i++){
                    dp[left][right]=max(dp[left][right],temp[left]*temp[i]*temp[right]+dp[left][i]+dp[i][right]);
                }
            }
        }
        return dp[0][n-1];
    }
};
```

# analysis
>这道题目是leetcode上面的hard难度的题目，我应该做不出来，所以就没为难自己了，直接上别人的代码.
题目中说明了边界情况，当气球周围没有气球的时候，旁边的数字按1算，这样我们可以在原数组两边各填充一个1，这样方便于计算。
这道题的最难点就是找递归式，如下所示：

dp[l][r] = max(dp[l][r], nums[l ]*nums[k]*nums[r] + dp[l][k] + dp[k][r]) 
dp[l][r]表示扎破(l, r)范围内所有气球获得的最大硬币数，不含边界

# reference
[312. Burst Balloons][1]
[LeetCode[312] Burst Balloons][2]
[[LeetCode] Burst Balloons 打气球游戏][3]

[1]: https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
[2]: https://segmentfault.com/a/1190000007297715
[3]: https://www.cnblogs.com/grandyang/p/5006441.html
