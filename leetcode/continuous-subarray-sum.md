# problem
>Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
```
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
```
Example 2:
```
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
```
Note:
1. The length of the array won't exceed 10,000.
2. You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

# codes
```
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int sum=0;
        for(int i=0;i<nums.size();i++){
            sum=nums[i];
            for(int j=i+1;j<nums.size();j++){
                sum+=nums[j];
                if(sum==k){
                    return true;
                }
                if(k!=0&&sum%k==0){
                    return true;
                }
            }
        }
        return false;
    }
};
```

# analysis
题目的意思是：给你一个数组，找出一个子数组，使得子数组之和能被n整除
- 思路也比较直接，把所有的子数组都列举出来然后判断是否符合条件就行了，这里需要用到两个循环，第一个循环表示子数组的开始位置，第二个循环表示子数组的结束位置。
# reference
[[LeetCode] Continuous Subarray Sum 连续的子数组之和][1]

[1]: https://www.cnblogs.com/grandyang/p/6504158.html