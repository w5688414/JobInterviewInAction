# problem
>Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
Example 1:
```
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```
Example 2:
```
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```
# codes
```
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int result=nums[0];
        vector<int> dp_max(nums.size(),0);
        vector<int> dp_min(nums.size(),0);
        dp_max[0]=dp_min[0]=nums[0];
        for(int i=1;i<nums.size();i++){
            dp_max[i]=max(nums[i],max(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i]));
            dp_min[i]=min(nums[i],min(dp_max[i-1]*nums[i],dp_min[i-1]*nums[i]));
            result=max(dp_max[i],result);
        }
        return result; 
    }
};
```

# analysis
>这个题目是一个动态规划的题目，我也没有写出来。
1）如果当前元素为正数，那么极大值只可能扩大，所以应该继续扩展当前subarray：
2）如果当前元素为负数，那么极大值可能会变小，所以不清楚应该继续扩展当前subarray还是新起一个subarray：
3）如果当前元素为0，那么包括一个0会使得极大值成为0，而按照操作规定，这里的极大值应该大于等于1，所以应该舍弃当前元素，新起一个subarray.
对于第2中情况，我们用两个数组分别记录遍历的极大值和极小值，因此最大值只可能从nums[i],mums[i]*dp_max[i-1],nums[i]*dp_min[i-1]中产生。想一想看是不是这个道理。


# reference
[[LeetCode] Maximum Product Subarray 求最大子数组乘积][1]
[[LeetCode] Maximum Product Subarray的4种解法][2]

[1]: https://www.cnblogs.com/grandyang/p/4028713.html
[2]: https://blog.csdn.net/whuwangyi/article/details/39577455
