# problem
> Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
Example 1:
```
Input: "1 + 1"
Output: 2
```
Example 2:
```
Input: " 2-1 + 2 "
Output: 3
```
Example 3:
```
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
```
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

# codes
```
class Solution {
public:
    int calculate(string s) {
        stack<int> nums,ops;
        int num=0;
        int result=0;
        int sign=1;
        for(char c:s){
            if(isdigit(c)){
                num=num*10+c-'0';
            }else{
                result+=sign*num;
                num=0;
                switch(c){
                    case '+':
                        sign=1;
                        break;
                    case '-':
                        sign=-1;
                        break;
                    case '(':
                        nums.push(result);
                        ops.push(sign);
                        result=0;
                        sign=1;
                        break;
                    case ')':
                        if(ops.size()>0){
                            result=ops.top()*result+nums.top();
                            nums.pop();
                            ops.pop();
                        }
                }  
            }
        }
        result+=sign*num;
        return result;  
    }
};
```

# analysis
>这是一道栈的题目，自己没做出来可能是没有经验。就是一个栈的模拟过程，把+，-符号当成数的正负值，然后依次相加就行，遇见左括号就入栈，遇见右括号就出栈

# reference
[224. Basic Calculator][1]

[1]: https://leetcode.com/problems/basic-calculator/discuss/62377/16-ms-solution-in-C++-with-stacks