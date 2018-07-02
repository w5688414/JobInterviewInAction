# problem
>We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.
```
Example :
Input: 
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```
Note:

- L, R  and A[i] will be an integer in the range [0, 10^9].
- The length of A will be in the range of [1, 50000].

# codes

## s1 failed
```
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        if(A.empty()){
            return 0;
        }
        vector<int> dp(A.size(),0);
        if(A[0]<=R&&A[0]>=L){
            dp[0]=1;
        }
        for(int i=1;i<A.size();i++){
            if(A[i]>R){
                dp[i]=dp[i-1];
            }else{
                dp[i]=dp[i-1]+1;
            }
        }
        return dp[A.size()-1];
    }
};
```

## s2
```
class Solution {
public:
    int numSubarrayBoundedMax(vector<int>& A, int L, int R) {
        int lastGreaterIndex = -1; // index where value > R
        int lastValidIndex = -1; // index where value >= L && value <=R
        int res = 0;
        for(int i=0; i < A.size(); i++)
        {
            if(A[i] >= L && A[i] <= R)
            {
                lastValidIndex = i;
                res += (i - lastGreaterIndex);
            }
            else if(A[i] < L)
            {
                res += max(0, ((i - lastGreaterIndex) - (i - lastValidIndex))) ;  
            }
            else
            {
                lastGreaterIndex = i;
            }
        }
        return res;
    }
};
```

# analysis
> 这道题我没做出来，还不怎么理解解法，以后有兴趣就完善一下。

# reference
[795. Number of Subarrays with Bounded Maximum][1]

[1]:https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/129294/C++-O(n)-solution