# problem
>Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 ="great":

```
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
```
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node"gr"and swap its two children, it produces a scrambled string"rgeat".
```
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
```
We say that"rgeat"is a scrambled string of"great".

Similarly, if we continue to swap the children of nodes"eat"and"at", it produces a scrambled string"rgtae".
```
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```
We say that"rgtae"is a scrambled string of"great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

# codes
```
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if(s1.size()!=s2.size()){
            return false;
        }
        int len=s1.length();
        //dp[k][i][j] 表示s2的从j开始长度为k的子串是否为s1的从i开始长度为k的子串的scramble string
        bool dp[len+1][len][len];
        memset(dp,0,sizeof(dp));
        //初始化dp[1][i][j],长度为1的子串，只要相等就是scramble string
        for(int i=0;i<len;i++){
            for(int j=0;j<len;j++){
                dp[1][i][j]=(s1[i]==s2[j]) ? true:false;
            }
        }
        for(int k=2;k<=len;k++){
            for(int i=0;i<=len-k;i++){
                for(int j=0;j<=len-k;j++){
                    //d表示长度为k的子串中，将子串一分为二的分割点
                    for(int d=1;d<k&&!dp[k][i][j];d++){
                        // dp[k][i][j] = true的条件是子串分割后的两段对应相等，或者交叉对应相等
                        if((dp[d][i][j]&&dp[k-d][i+d][j+d])||
                          (dp[d][i][j+k-d]&&dp[k-d][i+d][j])){
                            dp[k][i][j] = true;
                        }
                    }
                }
            }
        }
        return dp[len][0][0];
    }
};
```

# analysis
>没什么好说的，动态规划，不会
# reference
[[编程题]scramble-string][1]

[1]: https://www.nowcoder.com/questionTerminal/2bdc44bb0186468b8d8c13ea5d3a9e58
