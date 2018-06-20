# problem
>Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
Example:
```
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```
Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

# codes
```
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        if(nums.empty()){
            return 0;
        }
        int n=target+1;
        vector<int> dp(n,0);
        dp[0]=1;
        for(int i=1;i<n;i++){
            for(auto val:nums){
                if(i-val>=0){
                   dp[i]+=dp[i-val]; 
                }  
            }
        }
        return dp[target];
    }
};
```

# analysis
>dp[i]表示和为i的组合方法数，dp[target]就是我们所求的内容。然后上面的套路好像跟我以前做的题目类似，我只看了一眼答案，然后就把剩余的猜出来了。

# reference
[377. Combination Sum IV-动态规划][1]

[1]: https://blog.csdn.net/u011567017/article/details/52626439
