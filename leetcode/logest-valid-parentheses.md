# problem
>Given a string containing just the characters'('and')', find the length of the longest valid (well-formed) parentheses substring.

For"(()", the longest valid parentheses substring is"()", which has length = 2.

Another example is")()())", where the longest valid parentheses substring is"()()", which has length = 4.

# codes
```
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stack1;
        int last=-1;
        int len=0;
        // stack中保存左括弧的index
        for(int i=0;i<s.length();i++){
            if(s[i]=='('){ // 遇到左括弧就压栈
                stack1.push(i);
            }else{
                // 栈为空，更新起始点的位置
                if(stack1.empty()){
                    last=i;
                }else{
                    stack1.pop();
                    // 更新合法括弧的长度
                    if(stack1.size()){
                        int t=i-stack1.top();
                        len=max(len,t);
                    }else{
                        len=max(len,i-last);
                    }
                } 
            }
        }
        return len;
    }
};

```
```
class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stack1;
        int res=0;
        int start=0;
        for(int i=0;i<s.size();i++){
            if(s[i]=='('){
                stack1.push(i);
            }else if(s[i]==')'){
                if(stack1.empty()){
                    start=i+1;
                }else{
                    stack1.pop();
                    if(stack1.empty()){
                        res=max(res,i-start+1);
                    }else{
                        res=max(res,i-stack1.top());
                    }
                }
            }
        }
        return res;
    }
};
```

# analysis
>这是一道栈的题目，我开始尝试实现了一下，感觉自己水平还是不怎么够，主要思路是：遍历整个字符串，遇见做括号，就把左括号的索引压入栈中；如果遇见右括号，这时如果栈为空，说明没有左括号与之配对，则last就从该右括号开始，否则，从栈中取出一个括号，然后计算最大的长度。...看不明白我说的，直接看代码注释吧

# reference
[[编程题]longest-valid-parentheses][1]
[[LeetCode] Longest Valid Parentheses 最长有效括号][2]

[1]: https://www.nowcoder.com/questionTerminal/45fd68024a4c4e97a8d6c45fc61dc6ad
[2]: https://www.cnblogs.com/grandyang/p/4424731.html
