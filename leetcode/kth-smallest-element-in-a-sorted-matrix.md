# problem
>Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.

# codes
```
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<int> q;
        int m=matrix.size();
        int n=matrix[0].size();
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                q.emplace(matrix[i][j]);
                if(q.size()>k){
                    q.pop();
                }
            }
        }
        return q.top();
    }
};
```

# analysis
>这道题目用到了最大堆，我应该做不出来，想到了做法很简单。
使用一个最大堆，然后遍历数组每一个元素，将其加入堆，根据最大堆的性质，大的元素会排到最前面，然后我们看当前堆中的元素个数是否大于k，大于的话就将首元素去掉，循环结束后我们返回堆中的首元素即为所求:


# reference
[[LeetCode] Kth Smallest Element in a Sorted Matrix 有序矩阵中第K小的元素][1]

[1]: http://www.cnblogs.com/grandyang/p/5727892.html