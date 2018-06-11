# problem
>Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
Given target = 5, return true.

Given target = 20, return false.

# codes
```
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.size()==0){
            return false;
        }
        int rows=matrix.size();
        int cols=matrix[0].size();
        int i=0;
        int j=cols-1;
        while(i<rows&&j>=0){
            if(matrix[i][j]==target) return true;
            else if(matrix[i][j]<target){
                i++;
            }else{
                j--;
            }
        }
        return false;
    }
};
```

# analysis
>这道题目我会想到一个O(mlog(n))的解法，然后这题有一个O(m+n)的解法，从最右上角的一个元素开始比较，如果大了就向左，小了就向下，然后我验证了是正确的。还真是蛮神奇的。
# reference
[Search a 2D Matrix II][1]

[1]: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66247/Java-short-code-O(m+n)
