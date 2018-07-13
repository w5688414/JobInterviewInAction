# problem
>Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
```
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
```
Example 2:
```
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
```
Example 3:
```
Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
```

# codes
```
class Solution {
public:
    int maxProduct(vector<string>& words) {
        int res=0;
        vector<int> mask(words.size(),0);
        for(int i=0;i<words.size();i++){
            for(char c:words[i]){
                mask[i]|=1<<(c-'a');
            }
            for(int j=0;j<i;j++){
                if(!(mask[i]&mask[j])){
                    res=max(res,int(words[i].size()*words[j].size()));
                }
            }
        }
        return res;
    }
};
```

# analysis
>因为题目中说都是小写字母，那么只有26位，一个整型数int有32位，我们可以用后26位来对应26个字母，若为1，说明该对应位置的字母出现过，那么每个单词的都可由一个int数字表示，两个单词没有共同字母的条件是这两个int数相与为0。


# reference
[[LeetCode] Maximum Product of Word Lengths 单词长度的最大积][1]


[1]: http://www.cnblogs.com/grandyang/p/5090058.html