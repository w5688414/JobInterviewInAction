# problem
>We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
```
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
```
Example 2:
```
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
```
Note:

- 1 <= len(bits) <= 1000.
- bits[i] is always 0 or 1.

# codes
```
class Solution {
public:
    int minSteps(int n) {
        vector<int> dp(n+1,0);
        for(int i=2;i<=n;i++){
            dp[i]=i;
            for(int j=1;j<i;j++){
                if(i%j==0){
                    dp[i]=min(dp[i],i/j+dp[j]);
                }
            }
        }
        return dp[n];
    }
};
```

# analysis
>dp[n]表示第n个数需要的最小操作数。
找规律:
当n = 1时，已经有一个A了，我们不需要其他操作，返回0
当n = 2时，我们需要复制一次，粘贴一次，返回2
当n = 3时，我们需要复制一次，粘贴两次，返回3
当n = 4时，这就有两种做法，一种是我们需要复制一次，粘贴三次，共4步，另一种是先复制一次，粘贴一次，得到AA，然后再复制一次，粘贴一次，得到AAAA，两种方法都是返回4
当n = 5时，我们需要复制一次，粘贴四次，返回5
当n = 6时，我们需要复制一次，粘贴两次，得到AAA，再复制一次，粘贴一次，得到AAAAAA，共5步，返回5

1. 首先对于任意一个n(除了1以外)，我们最差的情况就是用n步，不会再多于n步，但是有可能是会小于n步的，比如n=6时，就只用了5步(先拼成AAA，再复制粘贴成了AAAAAA；或者先拼出AA，然后再复制一次，粘贴两次，得到的还是5).
2. 我们发现小模块的长度必须要能整除n，这样才能拆分

# reference
[[LeetCode] 2 Keys Keyboard 两键的键盘][1]

[1]: https://www.cnblogs.com/grandyang/p/7439616.html