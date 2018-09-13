# problem
>Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
Example 1:
```
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
```
Example 2:
```
Input: "aba"

Output: False
```
Example 3:
```
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

```

# codes

## s1
```
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int m=s.length();
        for(int i=m/2;i>=1;i--){
            if(m%i==0){
                int c=m/i;
                string t="";
                for(int j=0;j<c;j++){
                    t+=s.substr(0,i);
                }
                if(s==t) return true;
            }
        }
        return false;
    }
};
```
## s2
```
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        int i=1,j=0;
        int n=s.length();
        vector<int> dp(n+1,0);
        while(i<n){
            if(s[i]==s[j]){
                dp[++i]=++j;
            }else if(j==0){
                ++i;
            }else{
                j=dp[j];
            }
        }
        return dp[n]&&(dp[n]%(n-dp[n])==0);
    }
};
```

# analysis
## s1
>其实我在想一个问题，如果有一点思路的话，不妨大胆进行尝试，比如这题我也想到先枚举重复的长度，然后再进行计算的。
## s2
比如"abcabc"的dp数组为[0 0 0 0 1 2 3]，dp数组长度要比原字符串长度多一个。那么我们看最后一个位置数字为3，就表示重复的字符串的字符数有3个。如果是"abcabcabc"，那么dp数组为[0 0 0 0 1 2 3 4 5 6]，我们发现最后一个数字为6，那么表示重复的字符串为“abcabc”，有6个字符。那么怎么通过最后一个数字来知道原字符串是否由重复的子字符串组成的呢，首先当然是最后一个数字不能为0，而且还要满足dp[n] % (n - dp[n]) == 0才行，因为n - dp[n]是一个子字符串的长度，那么重复字符串的长度和肯定是一个子字符串的整数倍

# reference
[[LeetCode] Repeated Substring Pattern 重复子字符串模式][1]

[1]: http://www.cnblogs.com/grandyang/p/6087347.html