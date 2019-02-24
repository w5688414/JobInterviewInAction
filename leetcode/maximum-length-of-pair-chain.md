# problem
>You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
```
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
```
Note:
1. The number of given pairs will be in the range [1, 1000].

# codes
```
class Solution {
public:
    int findLongestChain(vector<vector<int>>& pairs) {
        sort(pairs.begin(),pairs.end(),[](vector<int>&a,vector<int>&b){
            return a[1]<b[1];
        });
        int n=pairs.size();
        vector<int> dp(n,1);
        for(int i=1;i<n;i++){
            for(int j=0;j<i;j++){
                if(pairs[i][0]>pairs[j][1]){
                    dp[i]=max(dp[i],dp[j]+1);
                }
            }
        }
        int ans=0;
        for(int i=0;i<dp.size();i++){
            ans=max(ans,dp[i]);
        }
        return ans;
    }
};
```

# analysis
>这是一个动态规划的题目，我也没有做出来。dp[i]代表前i个pair能够组成链对的最大长度，最后的结果就是遍历整的dp[i]得到最大值。


# reference
[[LeetCode] Maximum Length of Pair Chain 链对的最大长度][1]
[646. Maximum Length of Pair Chain][2]


[1]: https://www.cnblogs.com/grandyang/p/7381633.html
[2]: https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/131907/C++-DP-solution