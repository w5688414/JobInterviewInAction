# problem
>Implement wildcard pattern matching with support for'?'and'*'.
```
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
```

# codes
```
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        int m=strlen(s);
        int n=strlen(p);
        if(m==0&&n==0){
            return true;
        }
        if(m!=0&&n==0){
            return false;
        }
        bool dp[m+1][n+1];
        memset(dp,false,sizeof(dp));
        //初始状态：s="", p=""应该返回true
        dp[0][0]=true;
        //初始状态：s="", p="*"应该返回true
        for(int i=1;i<=n;i++){
            if(p[i-1]=='*'){
                dp[0][i]=dp[0][i-1];
            }
        }
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(s[i-1]==p[j-1]||p[j-1]=='?'){
                    dp[i][j]=dp[i-1][j-1];
                }else if(p[j-1]=='*'){
                    dp[i][j]=dp[i][j-1]||dp[i-1][j];
                }
            }            
        }
        return dp[m][n];
    }
};
```

# analysis
>想了一下还是用动态规划来实现吧，dp[i][j]表示s[i-1]与p[j-1]是否匹配。
递推关系式：
1.dp[i][j] = dp[i-1][j-1].   如果p[j-1]=='?' 或 s[i-1] == p[j-1]
2.dp[i][j] = dp[i-1][j] || dp[i][j-1].  dp[i-1][j]表示保留p中的*，可以匹配s中跟多字符,dp[i][j-1]表示p中的*匹配空字符
初始状态：s="", p=""应该返回true, s="", p="*"应该返回true, 其他初始状态如：s="", p="ab*"应该返回false
 */

# reference
[[编程题]wildcard-matching][1]

[1]: https://www.nowcoder.com/questionTerminal/e96f1a44d4e44d9ab6289ee080099322
