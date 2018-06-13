# problem
>Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
Example 1:
```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```
Example 2:
```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

# codes

```
class Solution {
public:
    int numSquares(int n) {
        while(n%4==0) n=n/4;
        if(n%8==7) return 4;
        for(int a=0;a*a<n;a++){
            int b=sqrt(n-a*a);
            if(a*a+b*b==n){
                return !!a+!!b;
            }
        }
        return 3;
    }
};
```
# analysis
>这道题目用了四数平方和定理，我翻答案了才知道；当然另一种解法是动态规划，后面我会拿出一周的时间专门攻克这种问题，这里介绍四数平方和定理，任意一个正整数均可表示为4个正整数的平方和，即结果只有1，2，3，4中的一个；然后可以化简，如果一个数里面含有因子4，可以除掉，不影响结果，自己验证；如果一个数除以8余7，则这个数肯定由四个数平方和组成，证明略；接下来我们就只需要判断是1，2，3个整数的平方和了。判断1个和2个整数的平方和很好判断，如代码，如果都不是那就是3个啦，如最后一行代码。

## reference
[[LeetCode] Perfect Squares 完全平方数][1]
[Summary of 4 different solutions (BFS, DP, static DP and mathematics)][2]


[1]: https://www.cnblogs.com/grandyang/p/4800552.html
[2]: https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)