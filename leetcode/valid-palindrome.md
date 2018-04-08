# problem
>Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama"is a palindrome.
"race a car"is not a palindrome.

Note: 
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

# codes
```
class Solution {
public:
    bool isPalindrome(string s) {
        if(s=="")
            return true;
        int begin=0;
        int end=s.size()-1;
        while(begin<=end){
            while(begin<end&&!isalnum(s[begin])){
                begin++;
            }
            while(end>begin&&!isalnum(s[end])){
                end--;
            }
            if(s[begin]==s[end]||tolower(s[begin])==tolower(s[end])){
                begin++;
                end--;
            }else{
                return false;
            }
        }
        return true;
    }
};

```

# analysis
>本题是判断回文子串，用两个索引，分别指向字符串的开头和结尾，其中注意大小写的相等比较，还有要跳过空格和标点不好。

# reference
[[编程题]valid-palindrome][1]


[1]: https://www.nowcoder.com/questionTerminal/b4dc0f1ee20448fca1f387fb1546f43f
