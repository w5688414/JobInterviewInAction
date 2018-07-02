# problem 1
>Given an input string, reverse the string word by word.
Example:
```
Input: "the sky is blue",
Output: "blue is sky the".
```
Note:
- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.

# codes
```
class Solution {
public:
    void reverseWords(string &s) {
        int m=s.length();
        reverse(s.begin(),s.end());
        int pre=0;
        for(int i=0;i<s.length();i++){
            if(s[i]!=' '){
                if(pre!=0){
                    s[pre]=' ';
                    pre++;
                }
                int j=i;
                while(j<m&&s[j]!=' '){
                    s[pre]=s[j];
                    pre++;
                    j++;
                }
                reverse(s.begin()+pre-(j-i),s.begin()+pre);
                i=j;
            }
        }
        s.resize(pre);
    }
    
};
```
# analysis
> 我开始用的是自己的reverse函数，然后也加入了去空格的操作，用了while，就是超时死活调不出来。后面改成这种for的方式就正常了，可能我自己对语言还理解不够深吧，希望后面能好一点。

# reference
[[LeetCode] Reverse Words in a String 翻转字符串中的单词][1]

[1]: http://www.cnblogs.com/grandyang/p/4606676.html