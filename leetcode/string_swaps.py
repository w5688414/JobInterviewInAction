from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list) -> str:
        d = defaultdict(list)
        for a,b in pairs:
            d[a].append(b)
            d[b].append(a)
        def dfs(x,A):
            if(x in d):
                A.append(x)
                for y in d.pop(x):
                    dfs(y,A)
        s=list(s)
        while(d):
            x=next(iter(d))
            A=[]
            dfs(x,A)
            print(A)
            A=sorted(A)
            B=sorted([s[i] for i in A])
            print(B)
            for i,b in enumerate(B):
                s[A[i]]=b
            
        return ''.join(s)

if __name__ == "__main__":
    solution=Solution()
    s = "dcab"
    pairs = [[0,3],[1,2]]
    ans=solution.smallestStringWithSwaps(s,pairs)
    print(ans)