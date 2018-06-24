# problem
>We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].  Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.  (A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.  It is guaranteed that the given input always makes it possible.

```
Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation: 
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
```
Note:
1. A, B are arrays with the same length, and that length will be in the range [1, 1000].
2. A[i], B[i] are integer values in the range [0, 2000].



# codes
```
class Solution {
public:
    int minSwap(vector<int>& A, vector<int>& B) {
        int n=A.size();
        vector<vector<int>> dp(n,vector<int>(2,INT_MAX));
        dp[0][0]=0;
        dp[0][1]=1;
        for(int i=1;i<n;i++){
            if(A[i-1]<A[i]&&B[i-1]<B[i]){
                dp[i][0]=min(dp[i][0],dp[i-1][0]);
                dp[i][1]=min(dp[i-1][1]+1,dp[i][1]);
            }
            if(A[i-1]<B[i]&&B[i-1]<A[i]){
                dp[i][0]=min(dp[i-1][1],dp[i][0]);
                dp[i][1]=min(dp[i-1][0]+1,dp[i][1]);
            }
        }
        return min(dp[n-1][0],dp[n-1][1]);
    }
};
```

# analysis
>用二维DP来计算：
- dp[i][0]表示不交换i，使得[0, i]严格递增的最小swap数
- dp[i][1]表示交换i，使得[0, i]严格递增的最小swap数
这道题目我也做不出来，我觉得这个解法我很喜欢，所以记录了下来。再看状态转移方程，在每一步判断，我们要不要交换，即使A[i-1]<A[i]&&B[i-1]<B[i]也可以交换，这是我没想到的，所以做不出来，看来还要历练。不知道这条路还要走多远，好像看不见尽头。

# reference
[801. Minimum Swaps To Make Sequences Increasing][1]

[1]: https://www.jianshu.com/p/9ab839a48d23
