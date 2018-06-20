# problem
>We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:
```
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
```
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

# codes
```
class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> dp(n+1,vector<int>(n+1,0));
        for(int i=2;i<=n;i++){
            for(int j=i-1;j>0;j--){
                int global_min=INT_MAX;
                for(int k=j+1;k<i;k++){
                    int local_max=max(dp[j][k-1],dp[k+1][i])+k;
                    global_min=min(global_min,local_max);
                }
                dp[j][i]=j+1==i ? j:global_min;
            }
        }
        return dp[1][n];
    }
};
```

# analysis
>这道题需要用到Minimax极小化极大算法，关于这个算法可以参见这篇讲解，并且题目中还说明了要用DP来做，那么我们需要建立一个二维的dp数组，其中dp[i][j]表示从数字i到j之间猜中任意一个数字最少需要花费的钱数，那么我们需要遍历每一段区间[j, i]，维护一个全局最小值global_min变量，然后遍历该区间中的每一个数字，计算局部最大值local_max = k + max(dp[j][k - 1], dp[k + 1][i])，这个正好是将该区间在每一个位置都分为两段，然后取当前位置的花费加上左右两段中较大的花费之和为局部最大值，为啥要取两者之间的较大值呢，因为我们要cover所有的情况，就得取最坏的情况。然后更新全局最小值，最后在更新dp[j][i]的时候看j和i是否是相邻的，相邻的话赋为i，否则赋为global_min。这里为啥又要取较小值呢，因为dp数组是求的[j, i]范围中的最低cost，比如只有两个数字1和2，那么肯定是猜1的cost低.

# reference
[[LeetCode] Guess Number Higher or Lower II 猜数字大小之二][1]

[1]: https://www.cnblogs.com/grandyang/p/5677550.html
