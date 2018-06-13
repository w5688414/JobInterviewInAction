# problem
>Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
 Example:
 ```
 Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

 ```



# codes
```
//递归超时
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        return getMin(grid,m-1,n-1);
    }
    int getMin(vector<vector<int>>& grid,int m,int n){
        if(m<0||n<0){
            return 0;
        }
        if(m==0&&n==0){
            return grid[0][0];
        }else if(m==0){
            return grid[m][n]+getMin(grid,m,n-1);
        }else if(n==0){
            return grid[m][n]+getMin(grid,m-1,n);
        }
        return min(getMin(grid,m-1,n),getMin(grid,m,n-1))+grid[m][n];
    }
};
```
```
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(i==0&&j==0){
                    grid[i][j]=grid[i][j];
                }else if(i==0){
                    grid[i][j]=grid[i][j-1]+grid[i][j];
                }else if(j==0){
                    grid[i][j]=grid[i-1][j]+grid[i][j];
                }else{
                    grid[i][j]=min(grid[i][j-1],grid[i-1][j])+grid[i][j];
                }
                
            }
        }
        return grid[m-1][n-1];
    }
 
};
```
# analysis
>递归的式子写出来了，但是超时；然后我把它换成非递归，好像是动态规划的过程，然后就解出来了。纪念一下做出来的第一道动态规划题。

# reference
[64. Minimum Path Sum][1]

[1]: https://leetcode.com/problems/minimum-path-sum/discuss/130863/C++-DP-solution
