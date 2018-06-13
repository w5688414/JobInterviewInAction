# problem
>Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

# codes
```
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char,int> book;
        for(int i=0;i<s.length();i++){
            book[s[i]]=-1;
        }
        int pre=-1;
        int max_len=0;
        for(int i=0;i<s.length();i++){
            pre=max(pre,book[s[i]]);
            max_len=max(max_len,i-pre);
            book[s[i]]=i;
        }
        return max_len;
    }
};
```
```
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len=0;
        int repeatIndex=-1;
        for(int i=0;i<s.length();i++){
            for(int j=i-1;j>=0;j--){
                if(s[i]==s[j]){
                    if(j>repeatIndex){
                        repeatIndex=j;
                    }
                    break;
                }
            }
            max_len=max(max_len,i-repeatIndex);
        }
        return max_len;
    }
};
```

# analysis
>我最开始也想到了用map，但是怎么也不会想到可以这么用，看来我是太肤浅了，map存储的是该字符串的坐标，初始为-1，有心的话好好想想这两个max的妙用。

- 遍历字符串，如果前面有重复的，就把前面离现在这个字符最近的字符的索引记录在repeatIndex中，如果没有重复，则也为repeatIndex。

# reference
[[编程题]longest-substring-without-repeating-characters][1]
[Longest Substring Without Repeating Characters][2]

[1]: https://www.nowcoder.com/questionTerminal/5947ddcc17cb4f09909efa7342780048
[2]: https://segmentfault.com/a/1190000004141853
