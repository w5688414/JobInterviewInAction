# problem
> Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
```
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

```
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

# codes
```
class Solution {
public:
    int addDigits(int num) {
        return (num-1)%9+1;
    }
};
```

# analysis
>我们先来观察1到20的所有的数根：

1    1
2    2
3    3
4    4
5    5
6    6
7    7
8    8    
9    9    
10    1
11    2
12    3    
13    4
14    5
15    6
16    7
17    8
18    9
19    1
20    2

根据上面的列举，我们可以得出规律，每9个一循环，所有大于9的数的树根都是对9取余，那么对于等于9的数对9取余就是0了，为了得到其本身，而且同样也要对大于9的数适用，我们就用(n-1)%9+1这个表达式来包括所有的情况。

# reference
[[LeetCode] Add Digits 加数字][1]

[1]: http://www.cnblogs.com/grandyang/p/4741028.html