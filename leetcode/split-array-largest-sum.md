# problem
>Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

- 1 ≤ n ≤ 1000
- 1 ≤ m ≤ min(50, n)

Examples:
```
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```

# codes
```
class Solution {
    
public:
    int splitArray(vector<int>& nums, int m) {
        int n=nums.size();
        vector<int> sums(n+1,0);
        vector<vector<int>> dp(m+1,vector<int>(n+1,INT_MAX));
        dp[0][0]=0;
        for(int i=1;i<=n;i++){
            sums[i]=sums[i-1]+nums[i-1];
        }
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                for(int k=i-1;k<j;k++){
                    int val=max(dp[i-1][k],sums[j]-sums[k]);
                    dp[i][j]=min(dp[i][j],val);
                }
            }
        }
        return dp[m][n];
    }
};

```

# analysis
- 如果将整个数组看为一个整体，那么最少有1组，所以i的范围是[1, j]，所以我们要遍历这中间所有的情况，假如中间任意一个位置k，dp[i-1][k]表示数组中前k个数字分成i-1组所能得到的最小的各个子数组中最大值，而sums[j]-sums[k]就是后面的数字之和，我们取二者之间的较大值，然后和dp[i][j]原有值进行对比，更新dp[i][j]为二者之中的较小值，

- 这样k在[1, j]的范围内扫过一遍，dp[i][j]就能更新到最小值，我们最终返回dp[m][n]即可

# reference
[[LeetCode] Split Array Largest Sum 分割数组的最大值][1]


[1]: https://www.cnblogs.com/grandyang/p/5933787.html
