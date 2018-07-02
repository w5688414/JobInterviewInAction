# problem
>Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
```
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 
```
Note:
1. Both strings' lengths will not exceed 100.
2. Only letters from a ~ z will appear in input strings.

# codes
```
class Solution {
public:
    int findLUSlength(string a, string b) {
       return a==b ? -1:max(a.length(),b.length());
    }
  
};
```

# analysis
>两个字符串的情况很少，如果两个字符串相等，那么一定没有非共同子序列，反之，如果两个字符串不等，那么较长的那个字符串就是最长非共同子序列.
原来只要分析足够就能很轻松的得到答案，看来我还是太年轻了。

# reference
[[LeetCode] Longest Uncommon Subsequence I 最长非共同子序列之一][1]


[1]: http://www.cnblogs.com/grandyang/p/6666839.html


