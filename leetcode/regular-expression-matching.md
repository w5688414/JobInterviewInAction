# problem
> Implement regular expression matching with support for'.'and'*'.
```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
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
        bool dp[m+1][n+1];
        memset(dp,false,sizeof(dp));
        dp[0][0]=true;
        for(int i=1;i<=n;i++){
            if(p[i-1]=='*'){
                dp[0][i]=dp[0][i-2];
            }
        }
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(s[i-1]==p[j-1]||p[j-1]=='.'){
                    dp[i][j]=dp[i-1][j-1];
                }else if(p[j-1]=='*'){
                    if(j!=1&&p[j-2]!='.'&&s[i-1]!=p[j-2]){
                        dp[i][j]=dp[i][j-2];
                    }else{
                        dp[i][j]=dp[i][j-1]||dp[i-1][j]||dp[i][j-2];
                    }
                }
            }
        }
        return dp[m][n];
    }
};
```

```
class Solution {
public:
    bool isMatch(string s, string p) {
        if(p.empty()) return s.empty();
        if(p.size()==1){
            return s.size()==1&&(s[0]==p[0]||p[0]=='.');
        }
        if(p[1]!='*'){
            if(s.empty()) return false;
            return (s[0]==p[0]||p[0]=='.')&&isMatch(s.substr(1),p.substr(1));
        }
        while(!s.empty()&&(s[0]==p[0]||p[0]=='.')){
            if(isMatch(s,p.substr(2))) return true;
            s=s.substr(1);
        }
        return isMatch(s,p.substr(2));
    }
};
```

# analysis
> 动态规划
    dp[i][j]表示s[i-1]与p[j-1]是否匹配
    如果 p[j-1] == s[i-1] || p[j-1] == '.', 此时dp[i][j] = dp[i-1][j-1];
    如果 p[j-1] == '*'
    分两种情况:
    1: 如果p[j-2] != s[i-1] && p[j-2] != '.', 此时dp[i][j] = dp[i][j-2] //*前面字符匹配0次
    2: 如果p[j-2] == s[i-1] || p[j-2] == '.'
        此时dp[i][j] = dp[i][j-2] // *前面字符匹配0次
        或者 dp[i][j] = dp[i][j-1] // *前面字符匹配1次
        或者 dp[i][j] = dp[i-1][j] // *前面字符匹配多次

这题用递归的话，大致思路如下：
1. 若p为空，s也为空，则返回true，否则返回false；
2. 若p的长度为1，s的长度也为1，且相同或p为‘.’，则返回true，否则返回false；
3. 若p的第二个字符不为*，此时s为空，则返回false，否则判断首字符是否匹配，且从各自的第二个字符开始调用递归函数；
4. 若p的第二个字符为*，若s不空且字符匹配，调用递归函数s和去掉前两个字符的p，若匹配，则返回true，否则s去掉首字母；
5. 返回调用递归函数匹配s和去掉前两个字符p的结果。

# reference
[[编程题]regular-expression-matching][1]
[[LeetCode] Regular Expression Matching 正则表达式匹配][2]

[1]: https://www.nowcoder.com/questionTerminal/d2ccc8cad7234aa5aa68c42471913b86
[2]: https://www.cnblogs.com/grandyang/p/4461713.html
