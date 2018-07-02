# problem 1
>Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
```
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
```
Restrictions:
1. The string consists of lower English letters only.
2. Length of the given string and k will in the range [1, 10000]

# codes
```
class Solution {
public:
    string reverseStr(string s, int k) {
        int n=s.length();
        int cnt=n/k;
        for(int i=0;i<=cnt;i++){
            if(i%2==0){
                if(i*k+k<n){
                    reverse(s.begin()+i*k,s.begin()+i*k+k);
                }else{
                    reverse(s.begin()+i*k,s.end());
                }
            }
        }
        return s;
    }
};
```

# analysis
>不知道是怎么的原因，这道题目我也没能做出来，我有点迷茫。看了答案，发现自己的思路并不清晰，肯能需要改进一下吧。

## reference
[[LeetCode] Reverse String II 翻转字符串之二][1]

[1]: http://www.cnblogs.com/grandyang/p/6583004.html