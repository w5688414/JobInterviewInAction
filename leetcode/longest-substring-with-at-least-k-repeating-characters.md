# problem
>Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.
Example 1:
```
Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
```
Example 2:
```
Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
```

# codes
```
class Solution {
public:
    int longestSubstring(string s, int k) {
        int hash[26]={0};
        int res=0;
        unordered_set<char> filter;
        for(auto c:s){
            hash[c-'a']++;
        }
        for(int i=0;i<26;i++){
            if(hash[i]>0&&hash[i]<k){
                filter.insert(i+'a');
            }
        }
        if(filter.empty()){
            return s.size();
        }
        if(filter.size()==s.length()){
            return 0;
        }
        int left=0;
        int right=0;
        int n=s.length();
        while(left<n&&right<n){
            while(left<n&&filter.find(s[left])!=filter.end()){
                left++;
            }
            right=left+1;
            while(right<n&&filter.find(s[right])==filter.end()){
                right++;
            }
            res=max(res,longestSubstring(s.substr(left,right-left),k));
            left=right;
        }
        return res;
    }
};
```

# analysis
>这道题目用了filter集合用来存储频率<k的字符，这样我们就判断一个子字符串里面是否包含这些字符来判断是否是合法的，如果包含，则不合法，如果不包含，则合法。为什么需要递归呢？
看看下面的样例，如果递归的话，则长度为5，实际上为0，这是因为有c字符干扰的缘故。

```
ababacb
3
```
# reference
[395. Longest Substring with At Least K Repeating Characters][1]


[1]: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/discuss/122969/C++-4ms
