# problem
>Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
```
Input: "aba", "cdc", "eae"
Output: 3
```
Note:

1. All the given strings' lengths will not exceed 10.
2. The length of the given list will be in the range of [2, 50].

# code

```
class Solution {
public:
    int findLUSlength(vector<string>& strs) {
        int n=strs.size();
        int res=-1;
        int i=0;
        int j=0;
        for(int i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(i==j){
                    continue;
                }
                if(isSub(strs[i],strs[j])){
                    break;
                }
            }
            if(j==n){
                res=max(res,(int)strs[i].length());
            }
        }
        return res;
    }
    
    bool isSub(string s1,string s2){
        int i=0;
        for(char c:s2){
            if(c==s1[i]){
                i++;
            }
            if(i==s1.length()) break;
        }
        return i==s1.length();
    }
};
```

# analysis
>这道题的暴力解法我也不会，不过我发现了一点，如果一个str是其他字符串的公共子集的话，函数就要返回-1；如果不是，那就是非公共子集，我们就找到了，我们更新res，来寻找最大的非公共子集。

# reference
[[LeetCode] Longest Uncommon Subsequence II 最长非共同子序列之二][1]

[1]: http://www.cnblogs.com/grandyang/p/6680548.html


