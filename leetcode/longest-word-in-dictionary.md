# problem
>Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
```
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
```
Example 2:
```
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
```
Note:

- All the strings in the input will only contain lowercase letters.
- The length of words will be in the range [1, 1000].
- The length of words[i] will be in the range [1, 30].

# code

```
class Solution {
public:
    string longestWord(vector<string>& words) {
        unordered_set<string> s(words.begin(),words.end());
        string res;
        int mxlen=0;
        for(string word:words){
            if(word.size()==1){
                solve(s,word,mxlen,res);
            }
        }
        return res;
    }
    void solve(unordered_set<string> s,string word,int& mxlen,string& res){
     if(word.size()>mxlen){
         mxlen=word.size();
         res=word;
     }else if(word.size()==mxlen){
         res=min(res,word);
     }
        for(char c='a';c<='z';c++){
            word.push_back(c);
            if(s.count(word)){
                solve(s,word,mxlen,res);
            }
            word.pop_back();
        }
    }
};
```

# analysis
>这是一个递归的实现，当然我没有实现出来，看来我的功力还是不够。当然还有更优的解法，后面再说吧。

# reference
[[LeetCode] Longest Word in Dictionary 字典中的最长单词][1]

[1]: http://www.cnblogs.com/grandyang/p/7817011.html

