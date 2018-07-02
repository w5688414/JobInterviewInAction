# problem
>Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.
Example 1:
```
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```
Note:
- 0 < nums.length <= 50000.
- 0 < nums[i] < 1000.
- 0 <= k < 10^6.

# codes
```
class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        if(k<=1){
            return 0;
        }
        int res=0;
        int mul=1;
        int left=0;
        for(int i=0;i<nums.size();i++){
            mul*=nums[i];
            while(mul>=k){
                mul=mul/nums[left];
                left++;
            }
            res+=i-left+1;
        }
        return res;
    }
};
```

# analysis
>开始想连乘保存到数组里面，后面会发现，连乘的数会很大，导致溢出。后面选择了这个滑动窗口的方式。

# reference
[[LeetCode] Subarray Product Less Than K 子数组乘积小于K][1]

[1]: http://www.cnblogs.com/grandyang/p/7753959.html
