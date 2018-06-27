# problem
>Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
Example 1:
```
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
```
Example 2:
```
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
```

# codes
```
class Solution {
private:
    vector<vector<int>> dirs = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        if(matrix.empty()||matrix[0].empty()){
            return 0;
        }
        int res=1;
        int m=matrix.size();
        int n=matrix[0].size();
        vector<vector<int>> dp(m,vector<int>(n,0));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                res=max(res,dfs(matrix,dp,i,j));
            }
        }
        return res;
    }
    int dfs(vector<vector<int>>& matrix,vector<vector<int>> &dp,int i,int j){
        if(dp[i][j]) return dp[i][j];
        int m=matrix.size();
        int n=matrix[0].size();
        int mx=1;
        for(auto a:dirs){
            int x=i+a[0];
            int y=j+a[1];
            if(x<0||x>=m||y<0||y>=n||matrix[x][y]<=matrix[i][j]){
                continue;
            }
            int len=1+dfs(matrix,dp,x,y);
            mx=max(mx,len);
        }
        dp[i][j]=mx;
        return mx;
    }
};

```

# analysis
>我还真以为是dynamic programming呢，原来是记忆化数组。不过我也写不出来这个东西。
dp[i][j]表示数组中以(i,j)为起点的最长递增路径的长度，初始将dp数组都赋为0，当我们用递归调用时，遇到某个位置(x, y), 如果dp[x][y]不为0的话，我们直接返回dp[x][y]即可，不需要重复计算。

# reference
[[LeetCode] Longest Increasing Path in a Matrix 矩阵中的最长递增路径][1]

[1]: https://www.cnblogs.com/grandyang/p/5148030.html
