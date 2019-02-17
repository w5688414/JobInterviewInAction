# problem
>Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie,"ACE"is a subsequence of"ABCDE"while"AEC"is not).

Here is an example:
S ="rabbbit", T ="rabbit"

Return3.

# codes

## 解法一
```
class Solution {
public:
    int numDistinct(string S, string T) {
        int len=T.size();
        vector<int> array(len+1);
        array[0]=1;
        for(int i=1;i<S.size()+1;i++){
            for(int j=min(i,len);j>0;j--){
                if(S[i-1]==T[j-1]){
                    array[j]=array[j]+array[j-1];
                }
            }
        }
        return array[len];
    }
};
```

## 解法二
```
class Solution {
public:
    int numDistinct(string s, string t) {
        int m=s.length();
        int n=t.length();
        if(m<n){
            return 0;
        }
        vector<vector<long>> dp(m+1,vector<long>(n+1,0));
        for(int i=0;i<=m;i++){
            for(int j=0;j<=n;j++){
                if(i==0&&j==0){
                    dp[i][j]=1;
                }else if(i==0){
                    dp[i][j]=0;
                }else if(j==0){
                    dp[i][j]=1;
                }else{
                    if(s[i-1]==t[j-1]){
                        dp[i][j]=dp[i-1][j-1]+dp[i-1][j];
                    }else {
                        dp[i][j]=dp[i-1][j];
                    }
                }
            }
        }
        return dp[m][n];
        
    }
};
```

# analysis
>解法一我不怎么懂，解法二，用二维数组来存储动态规划的中间状态，
>动态规划，定义dp[i][j]为字符串i变换到j的变换方法。
>如果S[i]==T[j]，那么dp[i][j] = dp[i-1][j-1] + dp[i-1][j]。意思是：如果当前S[i]==T[j]，那么当前这个字母即可以保留也可以抛弃，
>所以变换方法等于保留这个字母的变换方法加上不用这个字母的变换方法。
>如果S[i]!=T[i]，那么dp[i][j] = dp[i-1][j]，意思是如果当前字符不等，那么就只能抛弃当前这个字符。
>递归公式中用到的dp[0][0] = 1，dp[i][0] = 0（把任意一个字符串变换为一个空串只有一个方法）

# reference

[[编程题]distinct-subsequences][1]
[Leetcode Distinct Subsequences 解题报告][2]

[1]: https://www.nowcoder.com/questionTerminal/ed2923e49d3d495f8321aa46ade9f873
[2]: https://blog.csdn.net/worldwindjp/article/details/19770281