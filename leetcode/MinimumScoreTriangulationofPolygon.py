

class Solution:
    def minScoreTriangulation(self, A):
        n=len(A)
        dp=[[0]*n for i in range(n)]
        for d in range(2,n):
            for i in range(n-d):
                j=i+d
                for k in range(i+1,j):
                    if(dp[i][j]==0):
                        dp[i][j]=dp[i][k]+dp[k][j]+A[i]*A[k]*A[j]
                    else:
                        dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j]+A[i]*A[k]*A[j])
                print(dp)
        return dp[0][n-1]

if __name__ == "__main__":
    solution=Solution()
    arr=[1,3,1,4,1,5]
    res=solution.minScoreTriangulation(arr)
    print(res)