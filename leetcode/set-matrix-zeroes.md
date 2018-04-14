# problem
>Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(m n) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

# codes
```
class Solution {
public:
    void setZeroes(vector<vector<int> > &matrix) {
        int rows=matrix.size();
        int cols=matrix[0].size();
        bool row_flag=false;
        bool col_flag=false;
        //判断第一行和第一列是否有零，防止被覆盖
        for(int i=0;i<rows;i++){
            if(matrix[i][0]==0){
                row_flag=true;
                break;
            }
        }
        for(int i=0;i<cols;i++){
            if(matrix[0][i]==0){
                col_flag=true;
                break;
            }
        }
        //遍历矩阵，用第一行和第一列记录0的位置
        for(int i=1;i<rows;i++){
            for(int j=1;j<cols;j++){
                if(matrix[i][j]==0){
                    matrix[i][0]=0;
                    matrix[0][j]=0;
                }
            }
        }
        //根据记录清零
        for(int i=1;i<rows;i++){
            for(int j=1;j<cols;j++){
                if(matrix[i][0]==0||matrix[0][j]==0){
                    matrix[i][j]=0;
                }
            }
        }
        //最后处理第一行，第一列
        if(row_flag){
            for(int i=0;i<rows;i++){
                matrix[i][0]=0;
            }
        }
        if(col_flag){
            for(int i=0;i<cols;i++){
                matrix[0][i]=0;
            }
        }
    }
};
```

# analysis
>利用第一行第一列来存储该行和该列是否为0，详细解析见注释

# reference
[[编程题]set-matrix-zeroes][1]


[1]: https://www.nowcoder.com/questionTerminal/9ff9256075a1498fb165b583d951ebd4