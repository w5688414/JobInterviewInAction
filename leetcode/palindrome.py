class Solution:
    def canMakePaliQueries(self, s: str, queries: list):
        ans=[]
        d=len(s)
        n=len(queries)
        dp=[[0 for i in range(26)] for j in range(d+1)]
        for i in range(d):
            for j in range(26):
                dp[i+1][j]=dp[i][j]
            dp[i+1][ord(s[i])-ord('a')]+=1
        print(dp)
        for q in queries:
            start=q[0]
            end=q[1]
            k=q[2]
            cnt=0
            for i in range(26):
                cnt += (dp[end+1][i] - dp[start][i])%2
            ans.append(cnt//2 <= k)
            
        return ans

if __name__ == "__main__":
    solution=Solution()
    s="abcda"
    arr=[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
    ans=solution.canMakePaliQueries(s,arr)
    print(ans)