# problem
>Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s ="aab",
Return1since the palindrome partitioning["aa","b"]could be produced using 1 cut.

# codes
```
class Solution {
public:
// 使用动态规划来做    0,1,...,i,i+1,...,j,j+1 ,如果i~j是回文，则cut[j+1] = min(cut[j+1],cut[i]+1)
    int minCut(string s) {
        int len=s.size();
        vector<int> minCuts(len+1);
        minCuts[0]=-1;
        for(int i=1;i<=len;i++){
            minCuts[i]=minCuts[i-1]+1;
        }
        bool dp[len][len];
        fill_n(&dp[0][0],len*len,false);
        for(int j=1;j<len;j++){
            for(int i=j;i>=0;i--){
                if((s[i]==s[j])&&(j-i<2||dp[i+1][j-1])){
                    dp[i][j]=true;
                    minCuts[j+1]=min(minCuts[j+1],1+minCuts[i]);
                }
            }
        }
        return minCuts[len];
    }
};

```

# analysis
>定义状态数组: minCuts[n], minCuts[j]表示从0到j(包含j)的子串所需要用到的最小的切割次数
状态转移方程: 当子串str[i...j]是一个回文子串时, minCuts[j] = min(minCuts[i-1] + 1, minCuts[i])
动态规划，设字符串的的坐标为0,1,...,i,i+1,...,j,j+1。如果i~j是回文子串，那么最小切分次数等于前i个字符串的切分数+1，或者当前的切分数目。即cut[j+1] = min(cut[j+1],cut[i]+1)
# reference
[[编程题]palindrome-partitioning-ii][1]

[1]: https://www.nowcoder.com/questionTerminal/1025ffc2939547e39e8a38a955de1dd3