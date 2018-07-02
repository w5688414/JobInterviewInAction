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
>dp[n]表示第n个数需要的最小操作数。这道题我也用动态规划吧，毕竟需要多锻炼，还不太懂这些，我就用牛刀杀一下鸡。

# reference
[[LeetCode] 2 Keys Keyboard 两键的键盘][1]

[1]: https://www.cnblogs.com/grandyang/p/7439616.html