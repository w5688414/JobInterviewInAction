# problem
A(A也是他的编号)是一个孤傲的人，在一个n个人(其中编号依次为1到n)的队列中，他于其中的标号为b和标号c的人都有矛盾，所以他不会和他们站在相邻的位置。现在问你满足A的要求的对列有多少种？

给定人数n和三个人的标号A,b和c，请返回所求答案，保证人数小于等于11且大于等于3。
测试样例：
```
6,1,2,3
```
```
288
```

# codes
```
class LonelyA {
public:
    int getWays(int n, int A, int b, int c) {
        // write code here
        int res=1;
        for(int i=2;i<=n;i++){
            res*=i;
        }
        int B=1;
        for(int i=2;i<=n-1;i++){
            B*=i;
        }
        res-=B*2+B*2;
        B=1;
        for(int i=2;i<=n-2;i++){
            B*=i;
        }
        res+=B*2;
        return res;
    }
};
```

# analysis
总排法：n!
AB相邻：(n-1)!*2
AC相邻：(n-1)!*2
ABC相邻：(n-2)!*2
结果为：n!-(n-1)!*2-(n-1)!*2+(n-2)!*2

# reference
左成云课程