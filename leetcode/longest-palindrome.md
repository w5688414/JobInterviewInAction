# problem
>Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
```
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
```

# codes
```
class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char,int> m;
        for(int i=0;i<s.size();i++){
            m[s[i]]++;
        }
        int res=0;
        bool mid=false;
        for(auto s:m){
            if(s.second%2==0){
                res+=s.second;
            }else if(s.second%2==1){
                mid=true;
                res+=s.second;
                res--;
            }
        }
        return mid ? res+1:res;
    }
};
```

# analysis
>这道题目我大部分都是对的，但是没有考虑到如果统计字符是奇数的化，然后奇数-1，可以加进结果统计，导致出错，看来在严谨程度上有待提升。

# reference
[[LeetCode] Longest Palindrome 最长回文串][1]


[1]: http://www.cnblogs.com/grandyang/p/5931874.html