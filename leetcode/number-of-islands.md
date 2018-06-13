# problem
>Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
```
Input:
11110
11010
11000
00000

Output: 1
```
Example 2:
```
Input:
11000
11000
00100
00011

Output: 3
```


# codes
```
class Solution {
private:
    int d[4][2]={
         {-1, 0},{0, -1},{0, 1},{1, 0}
    };
public:
    int numIslands(vector<vector<char>>& grid) {
        if(grid.size()==0){
            return 0;
        }
        int rows=grid.size();
        int cols=grid[0].size();
        int count=0;
        for(int i=0;i<rows;i++){
            for(int j=0;j<cols;j++){
                if(grid[i][j]=='1'){
                    dfs(grid,i,j);
                    count++;
                }
            }
        }
        return count;
    }
    void dfs(vector<vector<char>>& grid,int i,int j){
        if(i<0||i>=grid.size()||j<0||j>=grid[0].size()){
            return;
        }
        if(grid[i][j]=='0'){
            return ;
        }
        grid[i][j]='0';
        for(int k=0;k<4;k++){
            dfs(grid,i+d[k][0],j+d[k][1]);
        }
    }
};
```

# analysis
>这道题就不多说了，几乎是我独立做出来的，dfs方法，感谢经历，感谢命运。
