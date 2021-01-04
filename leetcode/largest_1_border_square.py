class Solution:
    def largest1BorderedSquare(self, grid):
        m=len(grid)
        n=len(grid[0])
        top=[a[:] for a in grid]
        left=[a[:] for a in grid]
        for i in range(m):
            for j in range(n):
                if(grid[i][j]):
                    if(i):
                        top[i][j]=top[i-1][j]+1
                    if(j):
                        left[i][j]=left[i][j-1]+1
        print(left)
        print(top)
        for r in range(min(m,n),0,-1):
            for i in range(m-r+1):
                for j in range(n-r+1):
                    k=min(top[i+r-1][j],top[i+r-1][j+r-1])
                    k=min(k,left[i][j+r-1],left[i+r-1][j+r-1])
                    if(k>=r):
                        print(i+r-1)
                        print(j)
                        return r*r
        return 0

if __name__ == "__main__":
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    solution=Solution()
    res=solution.largest1BorderedSquare(grid)
    print(res)