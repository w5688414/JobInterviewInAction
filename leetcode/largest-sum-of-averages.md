# problem
>We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.
```
Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
```
Note:
1. 1 <= A.length <= 100.
2. 1 <= A[i] <= 10000.
3. 1 <= K <= A.length.
4. Answers within 10^-6 of the correct answer will be accepted as correct.

# codes

```
class Solution {
public:
    double largestSumOfAverages(vector<int>& A, int K) {
        int n=A.size();
        vector<double> sum(n+1,0);
        for(int i=1;i<=n;i++){
            sum[i]=A[i-1]+sum[i-1];
        }
        vector<vector<double>> dp(K,vector<double>(n,0));
        for(int k=0;k<K;k++){
            for(int i=0;i<n;i++){
                dp[k][i]=k==0 ? sum[i+1]/(i+1):dp[k-1][i];
                if(k>0){
                   for(int j=i-1;j>=0;j--){
                    dp[k][i]=max(dp[k][i],dp[k-1][j]+(sum[i+1]-sum[j+1])/(i-j));
                    } 
                } 
            }
        }
        return dp[K-1][n-1];
    }
};

```

# analysis
- dp[k][i]表示前i+1个元素(0~i)最多分k个组是平均数和最大,然后就是自己手动写一个表可以简单推导一下.表格如下:
k \ i	0	1	2	3	4
0	9.00	5.00	4.00	3.75	4.80
1	9.00	10.00	10.50	11.00	12.75
2	9.00	10.00	12.00	13.50	20.00

自己认认真真打完表后很容易就可以dp的方程:
dp[k][i] = max(dp[k - 1][i], dp[k - 1][j] + (sum[j + 1, i] / (i - j)); (k > = 1, sum[j + 1, i]表示区间j+1到i中间所有数的和)
当然求区间和的话我们可以做一下预处理保证sum[j+1,i]是O(1)时间就可以.

这个解法是我看得最懂的一次DP，因为它给了一个例子，然后归纳了打牌方程。

# reference
[Leetcode 813. Largest Sum of Averages][1]


[1]: https://www.jianshu.com/p/950a25796be3