# problem
>A message containing letters fromA-Zis being encoded to numbers using the following mapping:
```
'A' -> 1
'B' -> 2
...
'Z' -> 26
```
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message"12", it could be decoded as"AB"(1 2) or"L"(12).

The number of ways decoding"12"is 2.

# codes

```
class Solution {
public:
    int numDecodings(string s) {
       if(s.length()==0||s[0]=='0'){
           return 0;
       }
       int len=s.length();
       vector<int> dp(len+1,0); //dp[i] 表示i的字符的合法编码数量，取决于当前字符
       dp[0]=1; // 当有0个字符时候的编码个数，当有连续两个字符能编码时f[i] = f[i-2]，保证f[0]有值
       dp[1]=1; // 字符串长度为1时的编码个数
       for(int i=2;i<=len;i++){
           if(s[i-1]>='1'&&s[i-1]<='9'){
               dp[i]+=dp[i-1];
           }
           if(s[i-2]=='1'||s[i-2]=='2'&&s[i-1]>='0'&&s[i-1]<='6'){
               dp[i]+=dp[i-2];
           }
       }
        return dp[len];
    }

};
```

# analysis
>这个思想还不错，很好的利用了快慢指针和递归，快慢指针负责每次找根结点，然后建立根结点，递归负责建树，很巧妙。

# reference

[[编程题]convert-sorted-list-to-binary-search-tree][1]

[1]: https://www.nowcoder.com/questionTerminal/86343165c18a4069ab0ab30c32b1afd0