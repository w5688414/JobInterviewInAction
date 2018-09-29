# problem
>Given a matrix A, return the transpose of A.

The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:
```
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```
Example 2:
```
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```
Note:

1. 1 <= A.length <= 1000
2. 1 <= A[0].length <= 1000

# codes
```
class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        int m=A.size();
        int n=A[0].size();
        vector<vector<int>> res(n,vector<int>(m,0));
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                res[j][i]=A[i][j];
            }
        }
        return res;
    }
};
```

# analysis
>这道题虽然简单，但是很容易出错。注意m和n是不相等的这种情况，所以我们在做题的时候，要注意用res数组的大小要对应。

# reference
[Approach 1: Copy Directly][1]

[1]: https://leetcode.com/problems/transpose-matrix/solution/

