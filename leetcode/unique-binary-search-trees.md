# problem
>Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.
```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```
# codes
```
class Solution {
public:
    int numTrees(int n) {
        if(n<0){
            return -1;
        }
        int dp[n+1];
        dp[0]=1;
        dp[1]=1;
        for(int i=2;i<=n;i++){
            dp[i]=0;
            for(int j=0;j<i;j++){
                dp[i]+=dp[j]*dp[i-j-1];
            }
        }
        return dp[n];
    }
};

```

# analysis
>我设dp[i]表示共有i个节点时，能产生的BST树的个数
n == 0 时，空树的个数必然为1，因此dp[0] = 1
n == 1 时，只有1这个根节点，数量也为1，因此dp[1] = 1
因此，dp[2] = dp[0] * dp[1] + dp[1] * dp[0]
n == 3时，构造方法如题目给的示例所示，dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
同时，当根节点元素为 1, 2, 3, 4, 5, ..., i, ..., n时，基于以下原则的BST树具有唯一性：
以i为根节点时，其左子树构成为[0,...,i-1],其右子树构成为[i+1,...,n]构成
因此，dp[i] = sigma（dp[k] * dp[i-1-k]） 0 <= k < i - 1

# reference
[[编程题]unique-binary-search-trees][1]
[1]: https://www.nowcoder.com/questionTerminal/b2b6734cbc0b43088f6084785046b861