# problem
>Given an integer n, generate a square matrix filled with elements from 1 to n 2 in spiral order.

For example,
Given n =3,

You should return the following matrix:
```
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
```
# codes
```
class Solution {
public:
    vector<vector<int> > generateMatrix(int n) {
        vector<vector<int>> result;
        for(int i=0;i<n;i++){
            vector<int> ans(n,0);
            result.push_back(ans);
        }
        int num=1;
        int row=n-1;
        int row_start=0;
        int col_start=0;
        int col=n-1;
        while(col_start<=col&&row_start<=row){
            for(int i=col_start;i<=col;i++){
                result[row_start][i]=num;
                num++;
            }
            row_start++;
            for(int i=row_start;i<=row;i++){
                result[i][col]=num;
                num++;
            }
            col--;
            for(int i=col;i>=col_start;i--){
                result[row][i]=num;
                num++;
            }
            row--;
            for(int i=row;i>=row_start;i--){
                result[i][col_start]=num;
                num++;
            }
            col_start++;
        }
        return result;
        
    }
};

```

# analysis
>没什么好说的，这是我自己做出来的，纪念一下，这是第二次遇见这种题型了，算是一次巩固吧。
