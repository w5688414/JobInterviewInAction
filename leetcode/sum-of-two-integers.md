# problem
>Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.

# codes
```
class Solution {
public:
    int getSum(int a, int b) {
        if(b==0){
            return a;
        }
        int sum=a^b;
        int carry=(a&b)<<1;
        return getSum(sum,carry);
    }
};
```

# analysis
>我也想到用与或非运算，但是没想到代码居然这么简单，这是个递归的形式。学习一下大牛的代码。

# reference
[[LeetCode] Sum of Two Integers 两数之和][1]

[1]: https://www.cnblogs.com/grandyang/p/5631814.html