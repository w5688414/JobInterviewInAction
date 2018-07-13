# problem
>Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
```
Input: [5,7]
Output: 4
```
Example 2:
```
Input: [0,1]
Output: 0
```

# codes
```
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        int d=INT_MAX;
        while((m&d)!=(n&d)){
            d<<=1;
        }
        return m&d;
    }
};
```

# analysis
>我觉得这道题想到不容易。
[5, 7]里共有三个数字，分别写出它们的二进制为：

101　　110　　111

相与后的结果为100，仔细观察我们可以得出，最后的数是该数字范围内所有的数的左边共同的部分

再比如[26, 30]，它们的二进制如下：

11010　　11011　　11100　　11101　　11110

发现了规律后，我们只要写代码找到左边公共的部分即可，我们可以从建立一个32位都是1的mask，然后每次向左移一位，比较m和n是否相同，不同再继续左移一位，直至相同，然后把m和mask相与就是最终结果
# reference
[[LeetCode] Bitwise AND of Numbers Range 数字范围位相与][1]


[1]: http://www.cnblogs.com/grandyang/p/4431646.html