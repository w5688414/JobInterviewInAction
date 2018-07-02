# problem
>Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
```
Input: "aba"
Output: True
```
Example 2:
```
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
```
Note:
- The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# codes
```
class Solution {
public:
    bool validPalindrome(string s) {
        int left=0;
        int right=s.length()-1;
        while(left<right){
            if(s[left]!=s[right]){
                return isPalindrome(s,left+1,right)||isPalindrome(s,left,right-1);
            }
            left++;
            right--;
        }
        return true;
    }
    bool isPalindrome(string s,int start,int end){
        while(start<end){
            if(s[start]!=s[end]){
              return false;  
            }
            start++;
            end--;
        }
        return true;
    }
};

```

# analysis
>这道题虽然是easy的题目，我居然都写超时了，原来递归一下子就能解决，看来我还需要多加练习。

# reference
[[LeetCode] Valid Palindrome II 验证回文字符串之二][1]

[1]: http://www.cnblogs.com/grandyang/p/7618468.html