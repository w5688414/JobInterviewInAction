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
>dp[n]表示第n个数需要的最小操作数。这道题我也用动态规划吧，毕竟需要多锻炼，还不太懂这些，我就用牛刀杀一下鸡。

# reference
[[LeetCode] 2 Keys Keyboard 两键的键盘][1]

[1]: https://www.cnblogs.com/grandyang/p/7439616.html