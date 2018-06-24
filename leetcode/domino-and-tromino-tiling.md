# problem
>We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.
```
XX  <- domino

XX  <- "L" tromino
X
```
Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)
```
Example:
Input: 3
Output: 5
Explanation: 
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY
```

# codes
```
class Solution {
public:
    int numTilings(int N) {
        int M=1e9+7;
        vector<long> dp(N+1);
        dp[0]=1;
        dp[1]=1;
        dp[2]=2;
        for(int i=3;i<=N;i++){
            dp[i]=(dp[i-1]*2+dp[i-3])%M;
        }
        return dp[N];
    }
};
```

# analysis
>这道题我开始并没有看懂题目的意思，后面发现这个dp的推导过程也是奇葩，我感觉我做不出来，还是放弃了吧。
dp[n] = dp[n-1] + dp[n-2] + 2 * (dp[n-3] + ... + dp[0])

dp[n-1] = dp[n-2] + dp[n-3]+ 2 * (dp[n-4] + ... dp[0])

联立方程得：      
    dp[n]-dp[n-1] =  dp[n-3] + dp[n-1]
    dp[n]= 2 * dp[n-1] + dp[n-3]

# reference

[[LeetCode] Domino and Tromino Tiling 多米诺和三格骨牌][1]

[1]: http://www.cnblogs.com/grandyang/p/9179556.html
