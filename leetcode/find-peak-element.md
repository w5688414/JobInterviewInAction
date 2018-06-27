# problem
>A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.
Example 1:
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```
Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.

Note:

Your solution should be in logarithmic complexity.

# codes
```
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int left=0;
        int right=nums.size()-1;
        while(left<right){
            int mid=(left+right)/2;
            if(nums[mid]<nums[mid+1]){
                left=mid+1;
            }else{
                right=mid;
            }
        }
       return right;
    }
};
```

# analysis
>我写了一个O(n)的解法，但题目说要用O(log(n))的解法，没看清题意，不过从运行时间上来看，好像没快多少。

由于只是需要找到任意一个峰值，那么我们在确定二分查找折半后中间那个元素后，和紧跟的那个元素比较下大小，如果大于，则说明峰值在前面，如果小于则在后面。这样就可以找到一个峰值了.

# reference
[[LeetCode] Find Peak Element 求数组的局部峰值][1]

[1]: http://www.cnblogs.com/grandyang/p/4217175.html