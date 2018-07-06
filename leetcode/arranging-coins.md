# problem
>
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
```
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
```
Example 2:
```
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
```

# codes
```
class Solution {
public:
    int arrangeCoins(int n) {
        return int(-1+sqrt(1+8*(long)n))/2;
    }
};
```

# analysis
>一种数学解法O(1)，充分利用了等差数列的性质，我们建立等式, n = (1 + x) * x / 2, 我们用一元二次方程的求根公式可以得到 x = (-1 + sqrt(8 * n + 1)) / 2, 然后取整后就是能填满的行数.

还可以一行一行的累加，或者二分搜索，看来我还是太肤浅了。

# reference
[[LeetCode] Arranging Coins 排列硬币][1]

[1]: http://www.cnblogs.com/grandyang/p/6026066.html