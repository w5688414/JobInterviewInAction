# problem
>We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.
Example 1:
```
Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
```
Note:
1. 1 <= A.length <= 20
2. 1 <= A[0].length <= 20
3. A[i][j] is 0 or 1.

# codes
```
class Solution {
public:
    int matrixScore(vector<vector<int>>& A) {
        int m=A.size();
        int n=A[0].size();
        int res=0;
        for(int i=0;i<n;i++){
            int col=0;
            for(int j=0;j<m;j++){
                col+=A[j][i]^A[j][0];
            }
            res+=max(col,m-col)*(1<<(n-i-1));
        }
        return res;
    }
};
```

# analysis
>我还不是很懂这里面的原理，等有机会再想吧。
1所在的位置，决定了它对最终的得分的大小，当然越到矩阵的左边越好。最左边的1的个数比其他的数字更重要。因为我们要翻转最左边的列，使得其拥有最多的1。

## reference
[861. Score After Flipping Matrix][1]

[1]: https://leetcode.com/problems/score-after-flipping-matrix/solution/