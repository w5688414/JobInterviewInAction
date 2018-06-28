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
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n,vector<int>(n,0));
        int row=0;
        int col=0;
        int rows=n-1;
        int cols=n-1;
        int cnt=1;
        while(row<=rows&&col<=cols){
            for(int i=col;i<=cols;i++){
                res[row][i]=cnt;
                cnt++;
            }
            row++;
            for(int i=row;i<=rows;i++){
                res[i][cols]=cnt;
                cnt++;
            }
            cols--;
            for(int i=cols;i>=col;i--){
                res[rows][i]=cnt;
                cnt++;
            }
            rows--;
            for(int i=rows;i>=row;i--){
                res[i][col]=cnt;
                cnt++;
            }
            col++;
        }
        return res;
    }
};

```

# analysis
>没什么好说的，这是我自己做出来的，纪念一下，这是第二次遇见这种题型了，算是一次巩固吧。
