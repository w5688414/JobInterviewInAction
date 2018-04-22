# problem
>Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as1and0respectively in the grid.

For example,

There is one obstacle in the middle of a 3x3 grid as illustrated below.

```
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
```
The total number of unique paths is2.

Note: m and n will be at most 100.

# codes
```
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        int rows=obstacleGrid.size();
        int cols=obstacleGrid[0].size();
        vector<vector<int>> dp(rows,vector<int>(cols,0)); //初始化
        // 第一个格点的值与障碍数相反
        dp[0][0]=1-obstacleGrid[0][0];
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(obstacleGrid[i][j]==0){
                    if(i==0&&j!=0){
                        dp[0][j]=dp[0][j-1]; //左
                    }else if(i!=0&&j==0){
                        dp[i][0]=dp[i-1][0];  //上
                    }else if(i!=0&&j!=0){
                        dp[i][j]=dp[i][j]+dp[i-1][j]+dp[i][j-1]; //左+上
                    }
                }
            }
        }
        return dp[rows-1][cols-1];
    }
};

```

# analysis
>我高估了这个编程题目的难度，看完之后没什么难的，dp[i][j]代表dp[0][0]到dp[i][j]的路径数，开始时dp[0][0]为1，第一行和第一列的初始化参数都为1。dp[i][j]的路径数为dp[i-1][j]的路径数和dp[i][j-1]路径数之和。

# reference
[[编程题]unique-paths-ii][1]
[1]: https://www.nowcoder.com/questionTerminal/3cdf08dd4e974260921b712f0a5c8752