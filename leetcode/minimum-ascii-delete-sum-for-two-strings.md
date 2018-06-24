# problem
>Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
```
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
```
Example 2:
```
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
```
Note:
- 0 < s1.length, s2.length <= 1000.
- All elements of each string will have an ASCII value in [97, 122].

# codes
```
class Solution {
public:
    int minimumDeleteSum(string s1, string s2) {
        int m=s1.length();
        int n=s2.length();
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));
        for(int i=1;i<=m;i++){
            dp[i][0]=dp[i-1][0]+s1[i-1];
        }
        for(int j=1;j<=n;j++){
            dp[0][j]=dp[0][j-1]+s2[j-1];
        }
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(s1[i-1]==s2[j-1]){
                    dp[i][j]=dp[i-1][j-1];
                }else{
                    dp[i][j]=min(dp[i-1][j]+s1[i-1],dp[i][j-1]+s2[j-1]);
                }
            }
        }
        return dp[m][n];
    }
};
```

# analysis
>其中dp[i][j]表示字符串s1的前i个字符和字符串s2的前j个字符变成相等时所需要删除的最小ASCII码累加值。初始化的时候，有一个字符串为空的话，那么另一个字符串有多少字符就要删除多少字符，才能变成空字符串。初始化dp[0][j]和dp[i][0]，计算方法就是上一个dp值加上对应位置的字符，有点像计算累加数组的方法，由于字符就是用ASCII表示的，所以我们不用转int，直接累加就可以。

- 当对应位置的字符相等时，s1[i-1] == s2[j-1]，(注意由于dp数组的i和j是从1开始的，所以字符串中要减1)，那么我们直接赋值为上一个状态的dp值，即dp[i-1][j-1]，因为已经匹配上了，不用删除字符。如果s1[i-1] != s2[j-1]，那么就有两种情况，我们可以删除s[i-1]的字符，且加上被删除的字符的ASCII码到上一个状态的dp值中，即dp[i-1][j] + s1[i-1]，或者删除s[j-1]的字符，且加上被删除的字符的ASCII码到上一个状态的dp值中，即dp[i][j-1] + s2[j-1]。这不难理解吧，比如sea和eat，当首字符s和e失配了，那么有两种情况，要么删掉s，用ea和eat继续匹配，或者删掉e，用sea和at继续匹配，记住删掉的字符一定要累加到dp值中才行

# reference
[[LeetCode] Minimum ASCII Delete Sum for Two Strings 两个字符串的最小ASCII删除和][1]

[1]: http://www.cnblogs.com/grandyang/p/7752002.html