# problem
>Given a string representing an expression of fraction addition and subtraction, you need to return the calculation result in string format. The final result should be irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
```
Input:"-1/2+1/2"
Output: "0/1"
```
Example 2:
```
Input:"-1/2+1/2+1/3"
Output: "1/3"
```
Example 3:
```
Input:"1/3-1/2"
Output: "-1/6"
```
Example 4:
```
Input:"5/3+1/3"
Output: "2/1"
```
Note:
1. The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
2. Each fraction (input and output) has format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
3. The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1,10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
4. The number of given fractions will be in the range [1,10].
5. The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.

# codes
```
class Solution {
public:
    string fractionAddition(string expression) {
        istringstream is(expression);
        int num=0,dem=0,A=0,B=1;
        char c;
        while(is>>num>>c>>dem){
            A=A*dem+B*num;
            B=B*dem;
            int g=abs(gcd(A,B));
            A=A/g;
            B=B/g;
        }
        return to_string(A)+"/"+to_string(B);
    }
    int gcd(int a,int b){
        return b==0 ? a:gcd(b,a%b);
    }
};
```

# analysis
>这道题我写的有点复杂，果断放弃了，然后看了答案，发现用了isstringstream后变得好简洁，可能是功力不够，还需要锻炼一下吧。

# reference
[[LeetCode] Fraction Addition and Subtraction 分数加减法][1]
[1]: http://www.cnblogs.com/grandyang/p/6954197.html