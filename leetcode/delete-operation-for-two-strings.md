# problem
>Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.
Example 1:
```
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
```
Note:
1. The length of given words won't exceed 500.
2. Characters in given words can only be lower-case letters.


# codes

```
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m=word1.length();
        int n=word2.length();
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));
        for(int i=0;i<=m;i++){
            for(int j=0;j<=n;j++){
                if(i==0){
                    dp[i][j]=j;
                }else if(j==0){
                    dp[i][j]=i;
                }else if(word1[i-1]==word2[j-1]){
                    dp[i][j]=dp[i-1][j-1];
                }else{
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1]);
                }
            }
        }
        return dp[m][n];
    }
};
```

# analysis
>这是我做得最爽的一次dp题了。
- 由于我们dp数组的大小定义的是(m+1) x (n+1)，所以我们比较的是word1[i-1]和word2[j-1]
- 如果相同： dp[i][j] = dp[i-1][j-1] 
- 如果不同： dp[i][j]=1+min(dp[i-1][j],dp[i][j-1]);
其中dp[i][j]表示word1的前i个字符和word2的前j个字符组成的两个单词，能使其变相同的最小的步数。
"sea"和"eat"，当我们比较第一个字符，发现's'和'e'不相等，下一步就要错位比较啊，比较sea中第一个's'和eat中的'a'，sea中的'e'跟eat中的第一个'e'相比，这样我们的dp[i][j]就要取dp[i-1][j]跟dp[i][j-1]中的较小值，然后就直接得出结果了。

# reference
[[LeetCode] Delete Operation for Two Strings 两个字符串的删除操作][1]

[1]: http://www.cnblogs.com/grandyang/p/7144045.html