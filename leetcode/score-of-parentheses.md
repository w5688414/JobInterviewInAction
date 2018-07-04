# problem
>Given a balanced parentheses string S, compute the score of the string based on the following rule:

- () has score 1
- AB has score A + B, where A and B are balanced parentheses strings.
- (A) has score 2 * A, where A is a balanced parentheses string.
Example 1:
```
Input: "()"
Output: 1
```
Example 2:
```
Input: "(())"
Output: 2
```
Example 3:
```
Input: "()()"
Output: 2
```
Example 4:
```
Input: "(()(()))"
Output: 6
```
Note:

1. S is a balanced parentheses string, containing only ( and ).
2. 2 <= S.length <= 50

# codes
```
class Solution {
public:
    int scoreOfParentheses(string S) {
        return solve(S);
    }
    int solve(string s){
        if(s=="()"){
            return 1;
        }
        int cnt=0;
        for(int i=0;i<s.length()-1;i++){
            if(i>0&&cnt==0){
                return solve(s.substr(0,i))+solve(s.substr(i)); 
            }else if(s[i]=='('){
                cnt++;
            }else if(s[i]==')'){
                cnt--;
            }
        }
        return 2*solve(s.substr(1,s.size()-2));
    }
};
```

# analysis
>现在相比以前的一个进步是可以不照抄参考的代码，自己有独立的思想了，不过我在一些细节上还有待提升，不过这个解法加上记忆化数组能够缩短运行时间，有时间尝试一下，这是个标准的dfs。

## reference
[856. Score of Parentheses][1]

[1]: https://leetcode.com/problems/score-of-parentheses/discuss/142009/c++-dfs-with-memo