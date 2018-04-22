# problem
>Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

# codes

```
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m=word1.length();
        int n=word2.length();
        // dp[i][j]代表由word1的前i个子串变为word2的前j个子串的花费
        vector<vector<int> > dp(m+1,vector<int>(n+1,0));
        for(int i=1;i<=m;i++){
            dp[i][0]=i; // delete i chars of word1
        }
        for(int i=1;i<=n;i++){
            dp[0][i]=i;  // insert i chars of word2
        }
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                if(word1[i-1]==word2[j-1]){
                    dp[i][j]=dp[i-1][j-1];
                }else{
                    dp[i][j]=min(dp[i-1][j]+1,min(dp[i][j-1]+1,dp[i-1][j-1]+1)); // delete,insert,replace
                }
            }
        }
        return dp[m][n];
    }
};
```

# analysis
>动态规划，我不知道是怎么想出来的，我没办法。细节解析请看代码注释。


# reference

[[编程题]edit-distance][1]

[1]: https://www.nowcoder.com/questionTerminal/81d7738f954242e5ade5e65ec40e5027