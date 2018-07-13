# problem
> Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?

Credits:
Special thanks to @yukuairoy for adding this problem and creating all test cases.

# codes
```
class Solution {
public:
    bool isPowerOfFour(int num) {
        return num>0&&!(num&(num-1))&&(num&0x55555555);
    }
};
```

# analysis
>这道题可以用换底公式，如果能够写成x^4，log4(num)一定是整数。
另外，我们知道num & (num - 1)可以用来判断一个数是否为2的次方数，更进一步说，就是二进制表示下，只有最高位是1，那么由于是2的次方数，不一定是4的次方数，比如8，所以我们还要其他的限定条件，我们仔细观察可以发现，4的次方数的最高位的1都是计数位，那么我们只需与上一个数(0x55555555) <==> 1010101010101010101010101010101，如果得到的数还是其本身，则可以肯定其为4的次方数

# reference
[[LeetCode] Power of Four 判断4的次方数][1]

[1]: http://www.cnblogs.com/grandyang/p/5403783.html