# problem
>Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])


# codes
```
class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        vector<int> dp(n+1,0);
        dp[0]=1;
        for(int i=1;i<=n;i++){
            dp[i]=dp[i-1]+9*factorial(i-1);
        }
        return dp[n];
    }
    int factorial(int n){
        int res=1;
        for(int i=0;i<n;i++){
            res=res*(9-i);
        }
        return res;
    }
};
```

# analysis
>这道题让我们找一个范围内的各位上不相同的数字，比如123就是各位不相同的数字，而11,121,222就不是这样的数字。
- 一位数的满足要求的数字是10个(0到9)
- 二位数的满足题意的是81个,[10 - 99]这90个数字中去掉[11,22,33,44,55,66,77,88,99]这9个数字，还剩81个
- 通项公式为f(k) = 9 * 9 * 8 * ... (9 - k + 2)，那么我们就可以根据n的大小，把[1, n]区间位数通过通项公式算出来累加起来即可.

dp[0] = 1
dp[1] = 9x9 + dp[0]
dp[2] = 9x9x8 + dp[1]
dp[3] = 9x9x8x7 + dp[2] 


# reference

[357. Count Numbers with Unique Digits][1]
[[LeetCode] Count Numbers with Unique Digits 计算各位不相同的数字个数][2]

[1]: https://leetcode.com/problems/count-numbers-with-unique-digits/discuss/137608/C++-DP-beats-100
[2]: https://www.cnblogs.com/grandyang/p/5582633.html
