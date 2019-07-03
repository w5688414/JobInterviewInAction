# problem
>Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:
Input:
```
0 0 0
0 1 0
0 0 0
```
Output:
```
0 0 0
0 1 0
0 0 0
```
Example 2:
Input:
```
0 0 0
0 1 0
1 1 1
```
Output:
```
0 0 0
0 1 0
1 2 1
```
Note:
1. The number of elements of the given matrix will not exceed 10,000.
2. There are at least one 0 in the given matrix.
3. The cells are adjacent in only four directions: up, down, left and right.

# codes
## s1 有问题
```
class Solution {
private:
    vector<vector<int>> dirs{{-1,0},{1,0},{0,-1},{0,1}};
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int m=matrix.size();
        int n=matrix[0].size();
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]>0){
                   matrix[i][j]=update(matrix,i,j); 
                }
            }
        }
        return matrix;
    }
    int update(vector<vector<int>>& matrix,int i,int j){
        if(matrix[i][j]==0){
            return 0;
        }
        int m=matrix.size();
        int n=matrix[0].size();
        int res=INT_MAX;
        for(auto dir:dirs){
            int x=i+dir[0];
            int y=j+dir[1];
            if(x<0||x>=m||y<0||y>=n) continue;
            res=min(res,update(matrix,x,y)+1);
        }
        return res;
    }
};
```
## s2
```
class Solution {
private:
    vector<vector<int>> dirs{{-1,0},{1,0},{0,-1},{0,1}};
public:
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int m=matrix.size();
        int n=matrix[0].size();
        queue<pair<int,int>> q;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(matrix[i][j]==0){
                   q.push({i,j});
                }else{
                    matrix[i][j]=INT_MAX;
                }
            }
        }
        while(!q.empty()){
            auto t=q.front();
            q.pop();
            for(auto dir:dirs){
                int x=t.first+dir[0];
                int y=t.second+dir[1];
                if(x<0||x>=m||y<0||y>=n||matrix[x][y]<=matrix[t.first][t.second]) continue;
                matrix[x][y]=matrix[t.first][t.second]+1;
                q.push({x,y});
            }
        }
        return matrix;
    }

};
```

# analysis
>我们可以首先遍历一次矩阵，将值为0的点都存入queue，将值为1的点改为INT_MAX。
- 然后开始BFS遍历，从queue中取出一个数字，遍历其周围四个点，如果越界或者周围点的值小于等于当前值，则直接跳过。因为周围点的距离更小的话，就没有更新的必要，否则将周围点的值更新为当前值加1，然后把周围点的坐标加入queue.
然后我算了一下，确实是这样的。

# reference
[[LeetCode] 01 Matrix 零一矩阵][1]

[1]: http://www.cnblogs.com/grandyang/p/6602288.html

The International AAAI Conference on Web and Social Media
International Conference on Weblogs and Social Media 
Annual Conference on Neural Information Processing Systems
International Conference on Machine Learning


International Joint Conference on Artificial Intelligence

International Joint Conference on
Artificial Intelligence