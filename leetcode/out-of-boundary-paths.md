# problem
>There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:
```
Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
```

Example 2:
```
Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
```
Note:
1. Once you move the ball out of boundary, you cannot move it back.
2. The length and height of the grid is in range [1,50].
3. N is in range [0,50].

# codes
```
class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        vector<vector<vector<int>>> dp(N+1,vector<vector<int>>(m,vector<int>(n,0)));
        for(int k=1;k<=N;k++){
            for(int x=0;x<m;x++){
                for(int y=0;y<n;y++){
                    long long v1=(x==0) ? 1:dp[k-1][x-1][y];
                    long long v2=(x==m-1) ? 1:dp[k-1][x+1][y];
                    long long v3=(y==0) ? 1:dp[k-1][x][y-1];
                    long long v4=(y==n-1) ? 1: dp[k-1][x][y+1];
                    dp[k][x][y] = (v1 + v2 + v3 + v4) % 1000000007;
                }
            }
        }
        return dp[N][i][j];
    }
};
```

# analysis
>这道题用了三维dp数组，我也没有做出来，看来我太嫩了，没做出来。如果我失败了，我应该没有遗憾了。
dp[k][i][j]表示总共走k步，从(i,j)位置走出边界的总路径数
那么我们来找递推式，对于dp[k][i][j]，走k步出边界的总路径数等于其周围四个位置的走k-1步出边界的总路径数之和，如果周围某个位置已经出边界了，那么就直接加上1，否则就在dp数组中找出该值，这样整个更新下来，我们就能得出每一个位置走任意步数的出界路径数了，最后只要返回dp[N][i][j]就是所求结果了。

# reference
[[LeetCode] Out of Boundary Paths 出界的路径][1]

[1]: https://www.cnblogs.com/grandyang/p/6927921.html
