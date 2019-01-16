# problem
> Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

1. Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
2. Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.
Example 1:
```
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
```
Note:
1. The n will be in the range [1, 1000].

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