# problem
>Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

- B.length >= 3
- There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.
Example 1:
```
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
```
Example 2:
```
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
```
Note:

1. 0 <= A.length <= 10000
2. 0 <= A[i] <= 10000
Follow up:

- Can you solve it using only one pass?
- Can you solve it in O(1) space?

# codes
```
class Solution {
public:
    int longestMountain(vector<int>& A) {
        int n=A.size();
        int res=0;
        int base=0;
        while(base<n){
            int end=base;
            if(end+1<n&&A[end]<A[end+1]){
                while(end+1<n&&A[end]<A[end+1]) end++;  //up
                if(end+1<n&&A[end]>A[end+1]){
                    while(end+1<n&&A[end]>A[end+1]) end++;  //down
                    res=max(res,end-base+1);
                }
            }
            base=max(base+1,end);
        }
        return res;
    }
};
```

# analysis
>这道题我没有做出来，回头发现，也还是蛮简单的，关键是要读懂题意，先up后down，然后更新距离就行了哈。

# reference
[845. Longest Mountain in Array][1]


[1]: https://leetcode.com/problems/longest-mountain-in-array/solution/