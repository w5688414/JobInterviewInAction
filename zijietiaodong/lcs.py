

def LCS(str1,str2):
    '''
    不连续的公共子序列（不要求连续）
    '''
    m=len(str1)
    n=len(str2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                continue
            elif(str1[i-1]==str2[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]

def LCS_continuous(str1,str2):
    '''
    连续的公共子串（要求连续）
    '''
    m=len(str1)
    n=len(str2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    max_len=0
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                continue
            elif(str1[i-1]==str2[j-1]):
                dp[i][j]=dp[i-1][j-1]+1
                max_len=max(max_len,dp[i][j])
    return max_len

if __name__ == "__main__":
    # res=LCS("ABCBDAB", "BDCABA")
    # # BDAB
    # print(res)
    res=LCS("helloworld", "loop")
    # res=LCS_continuous("helloworld", "loop")
    print(res)