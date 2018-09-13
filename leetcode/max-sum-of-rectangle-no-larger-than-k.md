# problem
>Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
```
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2 
Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is 2,
             and 2 is the max number no larger than k (k = 2).
```
Note:

1. The rectangle inside the matrix must have an area > 0.
2. What if the number of rows is much larger than the number of columns?

# codes
```
class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        if(matrix.empty()||matrix[0].empty()){
            return 0;
        }
        int m=matrix.size(),n=matrix[0].size();
        int sum[m][n];
        int res=INT_MIN;
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                int t=matrix[i][j];
                if(i>0) t+=sum[i-1][j];
                if(j>0) t+=sum[i][j-1];
                if(i>0&&j>0) t-=sum[i-1][j-1];
                sum[i][j]=t;
                for(int r=0;r<=i;r++){
                    for(int c=0;c<=j;c++){
                        int d=sum[i][j];
                        if(r>0) d-=sum[r-1][j];
                        if(c>0) d-=sum[i][c-1];
                        if(r>0&&c>0){
                            d+=sum[r-1][c-1];
                        }
                        if(d<=k){
                            res=max(res,d);
                        }
                        
                    }
                }
            }
        }
        return res;
    }
};
```

# analysis
>说实话，我还真不大懂这一题，留着慢慢看吧。今后找个机会把这些东西全都整理下来。

## 2018／5/2
>这个解法有点暴力，不过在求sum的时候选择的思路比较好，我还是第一次见的这么求sum的。学习一下啦。

# reference
[[LeetCode] Max Sum of Rectangle No Larger Than K 最大矩阵和不超过K][1]


[1]:https://www.cnblogs.com/grandyang/p/5617660.html