# problem
如果更快的求一个整数k的n次方。如果两个整数相乘并得到结果的时间复杂度为O(1)，得到整数k的N次方的过程请实现时间复杂度为O(logN)的方法。

给定k和n，请返回k的n次方，为了防止溢出，请返回结果Mod 1000000007的值。

测试样例：
```
2,3
```
返回：8

# codes

```
class QuickPower {
public:
    int getPower(int k, int N) {
        // write code here
        if(N==0){
            return 1;
        }
        long temp=k;
        long res;
        for(int i=N;i>0;){
            if((i&1)!=0){
                res*=temp;
            }
            temp=(temp*temp)%(1000000007);
            res=res%1000000007;
            i=i>>1;
        }
        return (int)res;
    }
};
```

# analysis
>这道题的二分法我不怎么会，学习一下

# reference


