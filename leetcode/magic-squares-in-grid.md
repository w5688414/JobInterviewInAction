# problem
>A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:
```
Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
```
Note:

1. 1 <= grid.length <= 10
2. 1 <= grid[0].length <= 10
3. 0 <= grid[i][j] <= 15

# codes

## s1
```
class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int m=grid.size();
        int n=grid[0].size();
        int count=0;
        for(int i=0;i<m-2;i++){
            for(int j=0;j<n-2;j++){
              if(grid[i+1][j+1]==5&&isSubgrid(grid,i,j)){
                  count++;
              }
            }
        }
        return count;
    }
    bool isSubgrid(vector<vector<int>>& grid,int x,int y){
        int pre=15;
        int sum=0;
        //each row
        for(int i=x;i<x+3;i++){
            sum=0;
            for(int j=y;j<y+3;j++){
                if(grid[i][j]<0||grid[i][j]>9){
                    return false;
                }
                sum+=grid[i][j];
            }
            if(pre!=sum){
                return false;
            }
        }
        //each column
         for(int j=y;j<y+3;j++){
            sum=0;
            for(int i=x;i<x+3;i++){
                sum+=grid[i][j];
            }
            if(pre!=sum){
                return false;
            }
        }
        if(grid[x][y]+grid[x+1][y+1]+grid[x+2][y+2]!=pre){
            return false;
        }
        if(grid[x][y+2]+grid[x+1][y+1]+grid[x+2][y]!=pre){
            return false;
        }
        return true;
    }
};
```


# analysis
>没有调试成功，先放一放。


# reference
[840. Magic Squares In Grid][1]


[1]: https://leetcode.com/problems/magic-squares-in-grid/discuss/139980/4ms-C++-easy-solution-with-detail-explanation