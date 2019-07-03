# problem
> Given an integer, write a function to determine if it is a power of three.

Example 1:
```
Input: 27
Output: true
```
Example 2:
```
Input: 0
Output: false
```
Example 3:
```
Input: 9
Output: true
```
Example 4:
```
Input: 45
Output: false
```
Follow up:
Could you do it without using any loop / recursion?

# codes
```
class Solution {
public:
    bool isPowerOfThree(int n) {
        if(n<0){
            return false;
        }
        return int(log10(n)/log10(3))-log10(n)/log10(3)==0;
    }
};
```

# analysis
>利用对数的换底公式来做，高中学过的换底公式为logab = logcb / logca，那么如果n是3的倍数，则log3n一定是整数，我们利用换底公式可以写为log3n = log10n / log103，注意这里一定要用10为底数，不能用自然数或者2为底数

# reference
[[LeetCode] Power of Three 判断3的次方数][1]

[1]: https://www.cnblogs.com/grandyang/p/5138212.html