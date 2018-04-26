# problem
> Implement pow(x, n).

# codes
```
class Solution {
public:
    double pow(double x, int n) {
        if(n==0){
           return 1;
        }
        if(n<0){
            x=1/x;
            n=-n;
        }
        double result=1.0;
        while(n){
            if(n%2==1){
                result*=x;
            }
            n=n/2;
            x=x*x;
        }
        return result;
    }
};
```

# analysis
>如果n为0，直接返回1；如果为负数，则需要变为正数的指数乘法；指数乘法利用x^n=(x^(n/2))^2这样可以减少迭代次数。
# reference
[[编程题]powx-n][1]

[1]: https://www.nowcoder.com/questionTerminal/0616061711c944d7bd318fb7eaeda8f6
