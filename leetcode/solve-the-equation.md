# problem
>Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.
Example 1:
```
Input: "x+5-3+x=6+x-2"
Output: "x=2"
```
Example 2:
```
Input: "x=x"
Output: "Infinite solutions"
```
Example 3:
```
Input: "2x=x"
Output: "x=0"
```
Example 4:
```
Input: "2x+3x-6x=x+2"
Output: "x=-1"
```
Example 5:
```
Input: "x=x+2"
Output: "No solution"
```
# codes
```
class Solution {
public:
    string solveEquation(string equation) {
        int n=equation.size();
        int j=0;
        int sign=1;
        int b=0,a=0;
        for(int i=0;i<n;i++){
            if(equation[i]=='+'||equation[i]=='-'){
                if(i>j){
                    b+=stoi(equation.substr(j,i-j))*sign;  //连+，-符号一块儿截取
                }
                j=i;
            }else if(equation[i]=='x'){
                if(i==j||equation[i-1]=='+'){
                    a+=sign;
                }else if(equation[i-1]=='-'){
                    a-=sign;
                }else{
                    a+=stoi(equation.substr(j,i-j))*sign;
                }
                j=i+1;
            }else if(equation[i]=='='){
                if(i>j){
                    b+=stoi(equation.substr(j,i-j))*sign;
                }
                sign=-1;
                j=i+1;
            }
        }
        if(j<n) b+=stoi(equation.substr(j))*sign;
        if(a==0&&b==a) return "Infinite solutions";
        if(a==0&&a!=b) return "No solution";
        return "x="+to_string(-b/a);
    }
};
```

# analysis
>等式左边sign=1，等式右边sign=-1；b用来累加数，a用来累加符号x上的数。然后-b/a就是结果了哈，注意无解和无穷解的情况。无解a=0&&b!=0,无穷解a=0&&b=0。

然后这是一个字符串处理的问题，我也没做出来，看来我的思维的训练有待加强。

# reference
[[LeetCode] Solve the Equation 解方程][1]

[1]: http://www.cnblogs.com/grandyang/p/7350578.html