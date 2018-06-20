# problem
>Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

# codes
```
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int m=s.length();
        int n=t.length();
        int s1=0;
        int t1=0;
        while(s1<m&&t1<n){
            if(s[s1]==t[t1]){
                s1++;
                t1++;
            }else{
                t1++;
            }
        }
        return s1==m;
    }
};
```

# analysis
>我开始还以为是dp，原来简单的遍历字符串就行了，看来人有时候会钻牛角尖。

# reference
[[LeetCode] Is Subsequence 是子序列][1]

[1]: https://www.cnblogs.com/grandyang/p/5842033.html