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

## s1
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
## s2
```
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if(s1.length()!=s2.length()){
            return false;
        }
        if(s1==s2){
            return true;
        }
        string str1=s1;
        string str2=s2;
        sort(str1.begin(),str1.end());
        sort(str2.begin(),str2.end());
        if(str1!=str2){
            return false;
        }
        for(int i=1;i<s1.length();i++){
            string s11=s1.substr(0,i);
            string s12=s1.substr(i);
            string s21=s2.substr(0,i);
            string s22=s2.substr(i);
            if(isScramble(s11,s21)&&isScramble(s12,s22)){
                return true;
            }
            s21=s2.substr(s2.size()-i);
            s22=s2.substr(0,s2.size()-i);
            if(isScramble(s11,s21)&&isScramble(s12,s22)){
                return true;
            }
        }
        return false;
    }
};
```

# analysis
## s1
没什么好说的，动态规划，不会

## s2
递归的解法比dp的解法容易理解多了，感觉。我先从递归开始写起吧，不然感觉拿dp没办法。
如果s1和s2是scramble的话，那么必然存在一个在s1上的长度l1，将s1分成s11和s12两段，同样有s21和s22.那么要么s11和s21是scramble的并且s12和s22是scramble的；要么s11和s22是scramble的并且s12和s21是scramble的。
例如：
rgeat 和 great，rgeat 可分成 rg 和 eat 两段， great 可分成 gr 和 eat 两段，rg 和 gr 是scrambled的， eat 和 eat 当然是scrambled。
# reference
[[编程题]scramble-string][1]
[[LeetCode] Scramble String 爬行字符串][2]

[1]: https://www.nowcoder.com/questionTerminal/2bdc44bb0186468b8d8c13ea5d3a9e58
[2]: http://www.cnblogs.com/grandyang/p/4318500.html