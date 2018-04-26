# problem
>Divide two integers without using multiplication, division and mod operator.

# codes
```
class Solution {
public:
    int divide(int dividend, int divisor) {
        int count=0;
        int sum=0;
        bool flag=false;
        if(divisor==0){
            return -1;
        }
        if((dividend<0&&divisor>0)||(dividend>0&&divisor<0)){
            flag=true;
        }
        long long m=abs((long long)dividend);
        long long n=abs((long long)divisor);
        while(m>=n){
            long long t=n,i=1;
            while(t<<1<m){
                t=t<<1;
                i=i<<1;
            }
            m-=t;
            count+=i;
        }
        if(flag){
            return -count;
        }
        return count> INT_MAX ? INT_MAX:count;
    }
};
```

# analysis
>可以采用位运算进行优化，即模拟计算机上的除法运算。将整数转化成二进制形式，即num = a0*2^0 + a1*2^1 + a2*2^2 + ... + an*2^n。基于以上这个公式以及左移一位相当于乘以2，可以先让除数左移直到大于被除数之前得到一个最大的基数。然后每次用被除数去减去这个基数，同时结果增加2^k。接下来继续重新左移除数左移迭代，直到被除数不大于除数为止。因为这个方法的迭代次数是按2的幂直到结束，所以时间复杂度为O(logn)。
- 时间复杂度：O(logn)
- 空间复杂度：O(1)

# reference

[LeetCode --- 29. Divide Two Integers][1]

[1]: https://blog.csdn.net/makuiyu/article/details/43417749
