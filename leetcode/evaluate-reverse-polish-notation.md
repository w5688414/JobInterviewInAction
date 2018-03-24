# problem
>Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are+,-,*,/. Each operand may be an integer or another expression.

Some examples:
```
 ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
```
# codes
```
class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        stack<int>  stack1;
        bool flag=true;
        for(int i=0;i<tokens.size();i++){
            if(tokens[i][0]>='0'&&tokens[i][0]<='9'){
                int j=0;
                int number=0;
                while(tokens[i][j]!='\0'){
                    number=number*10+tokens[i][j]-'0';
                    j++;
                }
                stack1.push(number);
                continue;
            }
            switch(tokens[i][0]){
                case '+':
                    if(stack1.size()>1){
                        int num1=stack1.top();
                        stack1.pop();
                        int num2=stack1.top();
                        stack1.pop();
                        stack1.push(num1+num2);
                    }else{
                        return -1;
                    }
                    break;
               case '-':
                    if(tokens[i][1]!='\0'){
                        int j=1;
                        int number=0;
                        while(tokens[i][j]!='\0'){
                            number=number*10+tokens[i][j]-'0';
                            j++;
                        }
                        stack1.push(-number);
                        continue;
                    }
                    if(stack1.size()>1){
                        int num1=stack1.top();
                        stack1.pop();
                        int num2=stack1.top();
                        stack1.pop();
                        stack1.push(num2-num1);
                    }else{
                        return -1;
                    }                    
                    break;
               case '*':
                    if(stack1.size()>1){
                        int num1=stack1.top();
                        stack1.pop();
                        int num2=stack1.top();
                        stack1.pop();
                        stack1.push(num1*num2);
                    }else{
                        return -1;
                    }                    
                    break;
                case '/':
                    if(stack1.size()>1){
                        int num1=stack1.top();
                        stack1.pop();
                        int num2=stack1.top();
                        stack1.pop();
                        if(num1==0){
                            return -1;
                        }else{
                            stack1.push(num2/num1);
                        }
                    }else{
                        return -1;
                    }                    
                    break;
                default:
                    return -1;
            }
        }
        return stack1.top();
    }
};

```

# analysis
>纪念我自己调试出来的一道题目，思路没什么好讲的，代码写得不怎么简洁，以后有时间进行优化。