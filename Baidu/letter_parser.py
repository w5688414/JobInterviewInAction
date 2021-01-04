

class Solution():
    def __init__(self,):
        self.res=0

    def solve(self,s,j):
        if(j==len(s)):
            self.res+=1
        n=len(s)
        ans=[]
        s1=''
        for i in range(j,n):
            s1+=s[i]
            if(int(s1)<26):
                self.solve(s,j+len(s1))
            else:
                break

if __name__ == "__main__":
    
    s='1221'
    solution=Solution()
    solution.solve(s,0)
    print(solution.res)
    

