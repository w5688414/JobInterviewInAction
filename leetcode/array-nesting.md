# problem
>A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:
```
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
```
Note:
1. N is an integer within the range [1, 20,000].
2. The elements of A are all distinct.
3. Each element of A is an integer within the range [0, N-1].

# codes
```
class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n=nums.size();
        int res=0;
        vector<bool> visited(n,false);
        for(int i=0;i<n;i++){
            if(visited[i]){
                continue;
            }
            res=max(res,solve(nums,i,visited));
        }
        return res;
    }
    
    int solve(vector<int>& nums,int start, vector<bool>& visited){
        int i=start;
        int cnt=0;
        while(cnt==0||i!=start){
            visited[i]=true;
            i=nums[i];
            ++cnt;
        }
        return cnt;
    }
};
```

# analysis
>其实对于遍历过的数字，我们不用再将其当作开头来计算了，而是只对于未遍历过的数字当作嵌套数组的开头数字，不过在进行嵌套运算的时候，并不考虑中间的数字是否已经访问过，而是只要找到和起始位置相同的数字位置，然后更新结果res。

# reference
[[LeetCode] Array Nesting 数组嵌套][1]

[1]: http://www.cnblogs.com/grandyang/p/6932727.html