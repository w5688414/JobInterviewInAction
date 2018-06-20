# problem
>Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.

# codes

```
class Solution {
public:
    int integerBreak(int n) {
        if (n == 2 || n == 3) return n - 1;
        int res=1;
        while(n>4){
            res=res*3;
            n=n-3;
        }
        return res*n;
    }
};
```

# analysis
>我开始以为是一个动态规划的题目，然后发现是一个找规律的题目，想了老半天都没想出来，看来还需要历练。

# reference
[[LeetCode] Integer Break 整数拆分][1]

[1]: https://www.cnblogs.com/grandyang/p/5411919.html