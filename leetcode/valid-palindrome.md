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
        int i=0;
        int j=s.length()-1;
        while(i<=j){
            while(i<=j&&!isalnum(s[i])){
                i++;
            }
            while(i<=j&&!isalnum(s[j])){
                j--;
            }
            if(i>j){
                return true;
            }
            if(tolower(s[i])==tolower(s[j])){
                i++;
                j--;
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
这道题在牛课网上通过了但在leetcode上没有通过，"."和" "没有判断出来，我家了if(i>j)的操作，然后accept了，看来leetcode更难一点。

# reference
[[编程题]valid-palindrome][1]


[1]: https://www.nowcoder.com/questionTerminal/b4dc0f1ee20448fca1f387fb1546f43f
