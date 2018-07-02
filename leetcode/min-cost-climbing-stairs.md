# problem
>On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
Example 1:
```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```
Example 2:
```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```
Note:
1. cost will have a length in the range [2, 1000].
2. Every cost[i] will be an integer in the range [0, 999].

# codes

## s1
```
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n=cost.size();
        vector<int> dp(n+1,0);
        for(int i=2;i<=n;i++){
            dp[i]=min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1]);
        }
        return dp[n];
    }
};
```

# analysis
>这应该是最简单的dp问题了，但是还是没弄出来。
dp[i]表示爬到第i层的最小cost，有两种可能性，一个是从第i-2层上直接跳上来，一个是从第i-1层上跳上来。不会再有别的方法，所以我们的dp[i]只和前两层有关系，所以可以写做如下：

dp[i] = min(dp[i- 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

# reference
[[LeetCode] Min Cost Climbing Stairs 爬楼梯的最小损失][1]


[1]:http://www.cnblogs.com/grandyang/p/8343874.html
