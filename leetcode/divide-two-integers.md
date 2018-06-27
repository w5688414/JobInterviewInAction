# problem
>Divide two integers without using multiplication, division and mod operator.

# codes
```
class Solution {
public:
    int divide(int dividend, int divisor) {
        if(divisor==0||(dividend==INT_MIN&&divisor==-1)) return INT_MAX;
        long long m=abs((long long)dividend);
        long long n=abs((long long)divisor);
        int sign=1;
        if(dividend<0^divisor<0){
            sign=-1;
        }
        if(n==1) return m*sign;
        long long  res=0;
        while(m>=n){
            long long t=n,p=1;
            while(m>=(t<<1)){
                t<<=1;
                p<<=1;
            }
            res+=p;
            m-=t;
        }
        return res*sign;
    }
};
```

# analysis
>可以采用位运算进行优化，即模拟计算机上的除法运算。将整数转化成二进制形式，即num = a0*2^0 + a1*2^1 + a2*2^2 + ... + an*2^n。基于以上这个公式以及左移一位相当于乘以2，可以先让除数左移直到大于被除数之前得到一个最大的基数。然后每次用被除数去减去这个基数，同时结果增加2^k。接下来继续重新左移除数左移迭代，直到被除数不大于除数为止。因为这个方法的迭代次数是按2的幂直到结束，所以时间复杂度为O(logn)。
- 时间复杂度：O(logn)
- 空间复杂度：O(1)

# reference

[LeetCode --- 29. Divide Two Integers][1]
[[LeetCode] Divide Two Integers 两数相除][2]

[1]: https://blog.csdn.net/makuiyu/article/details/43417749
[2]: http://www.cnblogs.com/grandyang/p/4431949.html

