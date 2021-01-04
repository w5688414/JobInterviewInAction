# problem
> Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

Example 1:
```
Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
```
Example 2:
```
Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
```
Note:

1. 1 <= A.length = B.length <= 10000
2. 0 <= A[i] <= 10^9
3. 0 <= B[i] <= 10^9

# codes
```
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A1=sorted(A)
        B1=sorted(B)
        dict_A={}
        i=0
        remain=[]
        assigned={b:[] for b in B}
        for a in A1:
            if(a>B1[i]):
                assigned[B1[i]].append(a)
                i+=1
            else:
                remain.append(a)
        res=[]
        for b in B:
            if(assigned[b]):
                res.append(assigned[b].pop())
            else:
                res.append(remain.pop())
        return res
              
```

# analysis
>这道题目属于田忌赛马的题目，一开始就按照田忌赛马的思路做了，发现总是跟答案对不上，原来是顺序错了，要保持原来的顺序，
看来我还是需要苦练基本功，最近我在换成python，所以后面只有python的解析哈

# reference
[Approach 1: Greedy][1]

[1]: https://leetcode.com/problems/advantage-shuffle/solution/