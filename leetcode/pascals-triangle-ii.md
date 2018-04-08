# problem
>Given an index k, return the k th row of the Pascal's triangle.

For example, given k = 3,
Return[1,3,3,1].

Note: 
Could you optimize your algorithm to use only O(k) extra space?

# codes
```
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> result;
        int dp[rowIndex+1];
        memset(dp,0,sizeof(dp));
        dp[0]=1;
        for(int i=0;i<rowIndex;i++){
            for(int j=i+1;j>=1;j--){
                dp[j]+=dp[j-1];
            }
        }
        for(int i=0;i<rowIndex+1;i++){
            result.push_back(dp[i]);
        }
        return result;
    }
};

```

# analysis
>我开始直接推导数学公式了，后面发现根本没发编程，原来只是模拟一下杨辉三角的构建过程就行了，其中dp数组设置的很巧妙，这里注意，每一行的个数，等于index+1，画个图就知道了，index自顶向下，从0开始。
# reference
[[编程题]pascals-triangle-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/a60ee4a1c8a04c3a93f1de3cf9c16f19