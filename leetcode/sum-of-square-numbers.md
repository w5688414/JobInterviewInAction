# problem
>Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
```
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
```
Example 2:
```
Input: 3
Output: False
```

# codes
```
class Solution {
public:
    bool judgeSquareSum(int c) {
        for(int i=0;i<=sqrt(c);i++){
            int b=c-i*i;
            int j=sqrt(b);
            if(j*j==b){
                return true;
            }
        }
        return false;
    }
};
```

# analysis
>开始写的是i*i<c,后面来了一个非常大的数，导致溢出了，然后程序就跑超时了，看来溢出问题要特别注意。

# reference
[[LeetCode] Sum of Square Numbers 平方数之和][1]

[1]: http://www.cnblogs.com/grandyang/p/7190506.html