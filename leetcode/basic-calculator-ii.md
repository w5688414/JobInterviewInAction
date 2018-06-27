# problem
> Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:
```
Input: "3+2*2"
Output: 7
```
Example 2:
```
Input: " 3/2 "
Output: 1
```
Example 3:
```
Input: " 3+5 / 2 "
Output: 5
```
Note:

- You may assume that the given expression is always valid.
- Do not use the eval built-in library function.

# codes
```
class Solution {
public:
    int calculate(string s) {
        int m=s.length();
        int num=0;
        char op='+';
        stack<int> s1;
        for(int i=0;i<m;i++){
            if(s[i]>='0'){
                num=num*10+s[i]-'0';
            }
            if((s[i]<'0'&&s[i]!=' ')||i==m-1){
                if(op=='+'){
                    s1.push(num);
                }
                if(op=='-'){
                    s1.push(-num);
                }
                if(op=='*'||op=='/'){
                    int tmp=(op=='*') ? s1.top()*num:s1.top()/num;
                    s1.pop();
                    s1.push(tmp);
                }
                op=s[i];
                num=0;
            }
        }
        int res=0;
        while(!s1.empty()){
            res+=s1.top();
            s1.pop();
        }
        return res;
    }
};
```

# analysis
>这道题目我好像似曾相识，好像是paypal见过，当时被吊打，实在做不出来，后面发现+，-操作居然可以这样处理，好吧，我被征服了，这样我们只需要判断* /操作，这样就把问题大大化简了。 

# reference
[[LeetCode] Basic Calculator II 基本计算器之二][1]

[1]: http://www.cnblogs.com/grandyang/p/4601208.html