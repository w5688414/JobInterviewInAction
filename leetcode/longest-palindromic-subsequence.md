# problem
>Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:
```
"bbbab"
```
Output:
```
4
```
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
```
"cbbd"
```
Output:
```
2
```
One possible longest palindromic subsequence is "bb".

# codes
```
class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n=s.length();
        vector<vector<int>> dp(n,vector<int>(n,0));
        for(int i=n-1;i>=0;i--){
            dp[i][i]=1;
            for(int j=i+1;j<n;j++){
                if(s[i]==s[j]){
                    dp[i][j]=dp[i-1][j+1]+2;
                }else{
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1]);
                }
            }
        }
        return dp[0][n-1];
    }
};
```

# analysis
>这道题目用了dp的方法，dp[i][j]表示字符串位置i到位置j的最长回文子串的长度，我们从后往前遍历更新。
如果s[i]==s[j]，那么i和j就可以增加2个回文串的长度，我们知道中间dp[i + 1][j - 1]的值，那么其加上2就是dp[i][j]的值。如果s[i] != s[j]，那么我们可以去掉i或j其中的一个字符，然后比较两种情况下所剩的字符串谁dp值大，就赋给dp[i][j]，那么递推公式如下：

              /  dp[i + 1][j - 1] + 2                       if (s[i] == s[j])

dp[i][j] =

              \  max(dp[i + 1][j], dp[i][j - 1])        if (s[i] != s[j])

# reference
[[LeetCode] Longest Palindromic Subsequence 最长回文子序列][1]


[1]: https://www.cnblogs.com/grandyang/p/6493182.html


