# problem
> Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:
```
Input: [3,4,5,1,2] 
Output: 1
```
Example 2:
```
Input: [4,5,6,7,0,1,2]
Output: 0
```

# codes
```
class Solution {
public:
    int findMin(vector<int>& nums) {
        int m=nums.size();
        int low=0;
        int high=m-1;
        if(nums[low]>nums[high]){
            while(low!=(high-1)){
                int mid=(low+high)/2;
                if(nums[low]<nums[mid]){
                    low=mid;
                }else{
                    high=mid;
                }
            }
            return min(nums[low],nums[high]);
        }
        return nums[0];
    }
};
```

# analysis
>我们使用大小堆来解决问题，其中大堆保存右半段较大的数字，小堆保存左半段较小的数组。这样整个数组就被中间分为两段了，由于堆的保存方式是由大到小，我们希望大堆里面的数据是从小到大，这样取第一个来计算中位数方便。我们用到一个小技巧，就是存到大堆里的数先取反再存，这样由大到小存下来的顺序就是实际上我们想要的从小到大的顺序。当大堆和小堆中的数字一样多时，我们取出大堆小堆的首元素求平均值，当小堆元素多时，取小堆首元素为中位数.

 这是一个hard题目，我做不出来。

# reference
[[LeetCode] Find Minimum in Rotated Sorted Array 寻找旋转有序数组的最小值][1]

[1]: http://www.cnblogs.com/grandyang/p/4032934.html