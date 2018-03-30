# problem
>Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s ="leetcode",
dict =["leet", "code"].

Return true because"leetcode"can be segmented as"leet code".
# codes
```
class Solution {
public:
    bool wordBreak(string s, unordered_set<string> &dict) {
        int len=s.length();
        vector<bool> dp(len+1,false);
        dp[0]=true;
        for(int pos=0;pos<len;pos++){
            for(int i=pos;dp[pos]&&i<len;i++){
                if(dict.find(s.substr(pos,i-pos+1))!=dict.end()){
                    dp[i+1]=true;
                }
            }
        }
        return dp[len];
    }
};
```

# analysis
>dp[i] 表示源串的前i个字符可以满足分割，那么 dp[ j ] 满足分割的条件是存在k 使得 dp [k] && substr[k,j]在字典里。

# reference 
[[编程题]word-break][1]
[[Leetcode] Word Break、Word BreakII][2]

[1]: https://www.nowcoder.com/questionTerminal/5f3b7bf611764c8ba7868f3ed40d6b2c
[2]: https://blog.csdn.net/a83610312/article/details/12870501
