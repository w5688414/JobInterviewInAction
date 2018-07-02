# problem
>Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
5. An empty string is also valid.

Example 1:
```
Input: "()"
Output: True
```
Example 2:
```
Input: "(*)"
Output: True
```
Example 3:
```
Input: "(*))"
Output: True
```

Note:
1. The string size will be in the range [1, 100].

# codes
```
class Solution {
public:
    bool checkValidString(string s) {
        stack<int> s1,star;
        for(int i=0;i<s.length();i++){
            if(s[i]=='('){
                s1.push(i);
            }else if(s[i]==')'){
                if(s1.empty()&&star.empty()){
                    return false;
                }
                if(s1.empty()&&!star.empty()){
                    star.pop();
                }else{
                   s1.pop(); 
                }
                
            }else{
                star.push(i);
            }
        }
        while(!s1.empty()&&!star.empty()){
            if(s1.top()>star.top()){
                return false;
            }
            star.pop();
            s1.pop();
        }
        return s1.empty();
    }
};
```

# analysis
>这道题目我想到用了栈，但是没想到栈存放的是索引，在最后用来判断“*”能否消去s1里面的做括号，如果star的索引比s1的小，说明就不能当成右括号使用，直接返回false，这是我没有想到的一点。

# reference
[[LeetCode] Valid Parenthesis String 验证括号字符串][1]


[1]: http://www.cnblogs.com/grandyang/p/7617017.html