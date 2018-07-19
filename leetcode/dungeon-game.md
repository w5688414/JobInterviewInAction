# problem
>The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

Note:

- The knight's health has no upper bound.
- Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

# codes

```
class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        if(dungeon.size()==0){
            return 0;
        }
        int m=dungeon.size();
        int n=dungeon[0].size();
        vector<vector<int>> dp(m,vector<int>(n,0));
        dp[m-1][n-1]=max(1,1-dungeon[m-1][n-1]);
        for(int i=n-2;i>=0;i--){
            dp[m-1][i]=max(1,dp[m-1][i+1]-dungeon[m-1][i]);
        }
        for(int i=m-2;i>=0;i--){
            dp[i][n-1]=max(1,dp[i+1][n-1]-dungeon[i][n-1]);
        }
        for(int i=m-2;i>=0;i--){
            for(int j=n-2;j>=0;j--){
                int t=min(dp[i+1][j],dp[i][j+1]);
                dp[i][j]=max(1,t-dungeon[i][j]);
            }
        }
        return dp[0][0];
    }
};
```

# analysis
>来自小象学院的dp解法，我膜拜一下，从左下角反推到右上角，核心思想就是保证血量不少于1就行了。


# reference

[[LeetCode] Dungeon Game 地牢游戏][1]

[1]: http://www.cnblogs.com/grandyang/p/4233035.html