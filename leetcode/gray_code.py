class Solution:
    def circularPermutation(self, n: int, start: int):
        res=[]
        for i in range(1<<n):
            print(i>>1)
            print(i)
            t=start^i^(i>>1)
            res.append(t)
        return res


if __name__ == "__main__":
    solution=Solution()
    res=solution.circularPermutation(3,2)
    print(res)