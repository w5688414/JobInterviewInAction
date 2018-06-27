# problem
> Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
```
Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```

# codes

## solution 1
```
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int,int> m;
        for(int i=0;i<A.size();i++){
            for(int j=0;j<B.size();j++){
                m[A[i]+B[j]]++;
            }
        }
        int res=0;
        for(int i=0;i<C.size();i++){
            for(int j=0;j<D.size();j++){
                int target=-(C[i]+D[j]);
                res+=m[target];
            }
        }
        return res;
    }
};
```

# analysis
>自己只想出来O(n^4)的算法，O(n^2)的方法也挺简单，我们如果把A和B的两两之和都求出来，在哈希表中建立两数之和跟其出现次数之间的映射，那么我们再遍历C和D中任意两个数之和，我们只要看哈希表存不存在这两数之和的相反数就行了。
我并没有想到这个解法，但是确实很精妙。

# reference
[[LeetCode] 4Sum II 四数之和之二][1]

[1]: http://www.cnblogs.com/grandyang/p/6073317.html