# problem
>Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
```
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
```
Note:
1. 1 <= len(A), len(B) <= 1000
2. 0 <= A[i], B[i] < 100

# codes
```
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int m=A.size();
        int n=B.size();
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));
        int res=0;
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(A[i-1]==B[j-1]){
                    dp[i][j]=dp[i-1][j-1]+1;
                }
                res=max(res,dp[i][j]);
            }
        }
        return res;
    }
};
```

# analysis
>这道题的转移方程虽然简单，但是我也没有做出来。我们来看一个例子。
dp[i][j]表示数组A的前i个数字和数组B的前j个数字的最长子数组的长度，如果dp[i][j]不为0，则A中第i个数组和B中第j个数字必须相等，比对于这两个数组[1,2,2]和[3,1,2]，我们的dp数组为：
```
  3 1 2
1 0 1 0
2 0 0 2
2 0 0 1
```
我们注意观察，dp值不为0的地方，都是当A[i] == B[j]的地方，而且还要加上左上方的dp值，即dp[i-1][j-1]，所以当前的dp[i][j]就等于dp[i-1][j-1] + 1，而一旦A[i] != B[j]时，直接赋值为0，不用多想，因为子数组是要连续的，一旦不匹配了，就不能再增加长度了。我们每次算出一个dp值，都要用来更新结果res，这样就能得到最长相同子数组的长度了.

# reference
[[LeetCode] Maximum Length of Repeated Subarray 最长的重复子数组][1]

[1]: https://www.cnblogs.com/grandyang/p/7801533.html
