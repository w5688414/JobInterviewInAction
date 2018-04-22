# problem
>Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

```
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
```
You should return[1,2,3,6,9,8,7,4,5].

# codes
```
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int> > &matrix) {
        vector<int> result;
        if(!matrix.size() || !matrix[0].size())
            return result;
        int rows=matrix.size()-1;
        int cols=matrix[0].size()-1;
        int row_start=0;
        int col_start=0;
        while(row_start<=rows&&col_start<=cols){
            // Traverse Right
            for(int i=col_start;i<=cols;i++){
                result.push_back(matrix[row_start][i]);
            }
            row_start++;
            // Traverse Down
            for(int i=row_start;i<=rows;i++){
                result.push_back(matrix[i][cols]);
            }
            cols--;
            if(row_start<=rows){
                // Traverse Left
                for(int i=cols;i>=col_start;i--){
                    result.push_back(matrix[rows][i]);
                }
            }
            rows--;
            if(col_start<=cols){
                // Traverse Up
                for(int i=rows;i>=row_start;i--){
                    result.push_back(matrix[i][col_start]);
                }
            }
            col_start++;
        }
        return result;
    }
};

```

# analysis
>这里是一个常规的矩阵遍历做法，其中要注意矩阵判空，然后遍历矩阵的时候要考虑矩阵的行和列只有一行的情况。