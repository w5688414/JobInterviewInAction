# problem
>Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.
Example 1:
```
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
```
Note:
1. Then length of the input array is in range [1, 10,000].
2. The input array may contain duplicates, so ascending order here means <=.

# codes
```
class Solution {
public:
    int findUnsortedSubarray(vector<int>& nums) {
        int len=nums.size();
        int min_value=nums[len-1];
        int max_value=nums[0];
        int r=-1;
        int l=0;
        for(int i=0;i<nums.size();i++){
            max_value=max(nums[i],max_value);
            if(nums[i]<max_value){
                r=i;
            }
            min_value=min(nums[len-1-i],min_value);
            if(nums[len-1-i]>min_value){
                l=len-1-i;
            }
        }
        return r-l+1;
    }
};
```

# analysis
>从前往后寻找最大值，如果遇见元素小于前面的最大值，我们找到右边界；从后往前寻找最小值，如果遇见的元素大于前面的最小值，我们找到左边界。

# reference
[581. Shortest Unsorted Continuous Subarray][1]

[1]: https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/123732/Two-c++-solution