class Solution:
    def findTheLongestSubstring(self, s: str):
        vowels={'a':1,'e':2,'i':4,'o':8,'u':16}
        n=0
        d={0:-1}
        res=0
        for i,ch in enumerate(s):
            if(ch in vowels):
                n^=vowels[ch]
            if(n not in d):
                d[n]=i
            else:
                res=max(res,i-d[n])
            print(d)
        return res


if __name__ == "__main__":
    solution=Solution()
    s='eleetminicoworoep'
    res=solution.findTheLongestSubstring(s)
    print(res)