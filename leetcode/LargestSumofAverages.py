class Solution:
    def largestSumOfAverages(self, A, K: int):
        n=len(A)
        sums=[0]
        for i in range(n):
            sums.append(sums[-1]+A[i])
        
        dp=[0]*(n+1)
        for i in range(n):
            dp[i]=(sums[n]-sums[i])/(n-i)
        for k in range(K-1):
            for i in range(n):
                for j in range(i+1,n):
                    dp[i]=max(dp[i],dp[j]+(sums[j]-sums[i])/(j-i))
        print(dp)
        return dp[0]

if __name__ == "__main__":
    so=Solution()
    A=[9,1,2,3,9]
    K=3
    res=so.largestSumOfAverages(A,K)
    print(res)