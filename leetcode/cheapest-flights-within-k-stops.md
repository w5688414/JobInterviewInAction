# problem
>There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

```
Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
```
```
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
```
Note:
- The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
- The size of flights will be in range [0, n * (n - 1) / 2].
- The format of each flight will be (src, dst, price).
- The price of each flight will be in the range [1, 10000].
- k is in the range of [0, n - 1].
- There will not be any duplicated flights or self cycles.

# codes
```
class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int K) {
        vector<vector<int>> dp(K+2,vector<int>(n,1e9));
        dp[0][src]=0;
        for(int i=1;i<=K+1;i++){
            dp[i][src]=0;
            for(auto x:flights){
                dp[i][x[1]]=min(dp[i][x[1]],dp[i-1][x[0]]+x[2]);
            }
        }
        return (dp[K+1][dst]>=1e9) ? -1:dp[K+1][dst];
    }
};
```

# analysis
>这里我们使用一个二维DP数组，其中dp[i][j]表示最多飞i次航班到达j位置时的最少价格，那么dp[0][src]初始化为0，因为飞0次航班的价格都为0，转机K次，其实就是飞K+1次航班，我们开始遍历，i从1到K+1，每次dp[i][src]都初始化为0，因为在起点的价格也为0，然后即使遍历所有的航班x，更新dp[i][x[1]]，表示最多飞i次航班到达航班x的目的地的最低价格，用最多飞i-1次航班，到达航班x的起点的价格加上航班x的价格之和，二者中取较小值更新即可.

# reference
[[LeetCode] Cheapest Flights Within K Stops K次转机内的最便宜的航班][1]

[1]: http://www.cnblogs.com/grandyang/p/9109981.html