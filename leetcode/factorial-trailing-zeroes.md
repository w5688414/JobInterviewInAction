# problem
>Given an integer n, return the number of trailing zeroes in n!.
Example 1:
```
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```
Example 2:
```
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

# codes
```
class Solution {
public:
    int trailingZeroes(int n) {
        int res=0;
        while(n){
            res+=n/5;
            n=n/5;
        }
        return res;
    }
};
```

# analysis
>这道题目我感觉只要想明白了就很简单，2的个数远大于5的个数，所以只要统计5的个数就行了。

# reference
[[LeetCode] Factorial Trailing Zeroes 求阶乘末尾零的个数][1]

[1]: http://www.cnblogs.com/grandyang/p/4219878.html
