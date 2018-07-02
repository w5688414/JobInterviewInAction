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

# analysis
>其实我在想一个问题，如果有一点思路的话，不妨大胆进行尝试，比如这题我也想到先枚举重复的长度，然后再进行计算的。

# reference
[[LeetCode] Repeated Substring Pattern 重复子字符串模式][1]

[1]: http://www.cnblogs.com/grandyang/p/6087347.html