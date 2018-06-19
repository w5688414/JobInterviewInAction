# problem
>You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
Example 1:
```
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```
Example 2:
```
Input: coins = [2], amount = 3
Output: -1
```
Note:
You may assume that you have an infinite number of each kind of coin.

# codes
```
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1,0x7ffffffe);
        dp[0]=0;
        for(auto coin:coins){
            for(int i=1;i<=amount;i++){
                if(i-coin>=0){
                    dp[i]=min(dp[i-coin]+1,dp[i]); 
                }
            }
        }
        return dp[amount]==0x7ffffffe ? -1: dp[amount];
    }
};
```

# analysis
>这是一道动态规划的题目，我现在也要尝试写动态规划的方法，发现代码好简单，关键是要注意很多细节，dp[i]表示凑齐钱数i所需要的最小硬币数，dp[i]就是当前i最小钱数和i-coin的最小硬币数的最小值。

# reference
[leetcode 322. Coin Change-硬币交换|动态规划][1]

[1]: https://blog.csdn.net/happyaaaaaaaaaaa/article/details/50976088