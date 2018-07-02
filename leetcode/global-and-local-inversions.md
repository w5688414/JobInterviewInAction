# problem
>We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.
Example 1:
```
Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.
```
Example 2:
```
Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
```
Note:

- A will be a permutation of [0, 1, ..., A.length - 1].
- A will have length in range [1, 5000].
- The time limit for this problem has been reduced.


# codes
```
class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        int n=A.size();
        int min_value=INT_MAX;
        for(int i=n-1;i>=2;i--){
            min_value=min(min_value,A[i]);
            if(A[i-2]>min_value) return false;
        }
        return true;
    }
};
```

# analysis
>我们可以发现，其实局部倒置是全局倒置的一种特殊情况，即局部倒置一定是全局倒置，而全局倒置不一定是局部倒置。

题目让我们判断该数组的全局倒置和局部倒置的个数是否相同，那么我们想，什么情况下会不相同？如果所有的倒置都是局部倒置，那么由于局部倒置一定是全局倒置，则二者个数一定相等。如果出现某个全局倒置不是局部倒置的情况，那么二者的个数一定不会相等。

所以问题的焦点就变成了是否能找出不是局部倒置的全局倒置。所以为了和局部倒置区别开来，我们不能比较相邻的两个，而是至少要隔一个来比较。我们可以从后往前遍历数组，遍历到第三个数字停止，然后维护一个 [i, n-1] 范围内的最小值，每次和 A[i - 2] 比较，如果小于 A[i - 2]，说明这是个全局的倒置，并且不是局部倒置，那么我们直接返回false即可。

# reference
[[LeetCode] Global and Local Inversions 全局与局部的倒置][1]

[1]: http://www.cnblogs.com/grandyang/p/8983098.html