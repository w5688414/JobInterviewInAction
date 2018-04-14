# problem
>Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 ="aabcc",
s2 ="dbbca",

When s3 ="aadbbcbcac", return true.
When s3 ="aadbbbaccc", return false.

# codes
```
class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        int l1=s1.length();
        int l2=s2.length();
        int l3=s3.length();
        if(l1+l2!=l3){
            return false;
        }
        vector<vector<bool>> dp(l1+1,vector<bool>(l2+1,false));
        dp[0][0]=true;
        for(int i=1;i<=l1;i++){
            dp[i][0]=dp[i-1][0]&&s1[i-1]==s3[i-1];
        }
        for(int j=1;j<=l2;j++){
            dp[0][j]=dp[0][j-1]&&s2[j-1]==s3[j-1];
        }
        for(int i=1;i<=l1;i++){
            for(int j=1;j<=l2;j++){
                dp[i][j]=(dp[i-1][j]&&s1[i-1]==s3[i+j-1]||
                          dp[i][j-1]&&s2[j-1]==s3[i+j-1]);
            }
        }
        return dp[l1][l2];
    }
};

```

# analysis
>动态规划，不懂
s3是由s1和s2交织生成的，意味着s3由s1和s2组成，在s3中s1和s2字符的顺序是不能变化的，和子序列题型类似，这种题我们一般是用动态规划来解。
1. 设dp[i][j]表示s3的前i+j个字符可以由s1的前i个字符和s2的前j个字符交织而成。
2. 状态转移方程：有两种情况
2.1 第一个状态转移方程：
dp[i][j]= (dp[i - 1][j] && s1[i - 1] == s3[i + j - 1]
dp[i-1][j]表示若s3的前i+j-1个字符能够由s1前i-1个字符和s2的前j个字符交织而成，那么只需要s1的第i个字符与s3的第i+j个字符相等，那么dp[i][j]=true;
2.2 第二个状态转移方程：

dp[i][j]= dp[i][j-1] && s2[j - 1] == s3[i + j - 1]
dp[i-1][j]表示若s3的前i+j-1个字符能够由s1前i个字符和s2的前j-1个字符交织而成，那么只需要s2的第j个字符与s3的第i+j个字符相等，那么dp[i][j]=true;


# reference
[[编程题]interleaving-string][1]

[1]: https://www.nowcoder.com/questionTerminal/4d0f94617e454e2da23e660cded4d9e8