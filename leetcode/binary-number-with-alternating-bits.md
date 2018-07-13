# problem
>Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
Example 1:
```
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
```
Example 2:
```
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
```
Example 3:
```
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
```
Example 4:
```
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
```

# codes
```
class Solution {
public:
    bool hasAlternatingBits(int n) {
        int d=n&1;
        while((n&1)==d){
            d^=1;
            n>>=1;
        }
        return n==0;
    }
};
```

# analysis
>我想的方式和这个类似，但是没有想到右移一位来解决这个问题。

# reference
[[LeetCode] Binary Number with Alternating Bits 有交替位的二进制数][1]

[1]: http://www.cnblogs.com/grandyang/p/7696387.html