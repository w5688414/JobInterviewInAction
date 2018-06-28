# problem
>Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.
Example 1:
```
Input: [1,3,5]
Output: 1
```
Example 2:
```
Input: [2,2,2,0,1]
Output: 0
```

# codes
```
class Solution {
public:
    int findMin(vector<int>& nums) {
        int low=0;
        int high=nums.size()-1;
        int res=INT_MAX;
        while(low<high-1){
            int mid=(low+high)/2;
            if(nums[low]<nums[mid]){
                res=min(nums[low],res);
                low=mid+1;
            }else if(nums[low]>nums[mid]){
                res=min(res,nums[mid]);
                high=mid;
            }else{
                low++;
            }
        }
        res = min(res, nums[low]);
        res = min(res, nums[high]);
        return res;
    }
};
```

# analysis
>hard题目+1,我也做不出来，也不明白里面的原理。
当数组中存在大量的重复数字时，就会破坏二分查找法的机制，我们无法取得O(lgn)的时间复杂度，又将会回到简单粗暴的O(n)，比如如下两种情况：

{2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 2} 和 {2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2}， 我们发现，当第一个数字和最后一个数字，还有中间那个数字全部相等的时候，二分查找法就崩溃了，因为它无法判断到底该去左半边还是右半边。这种情况下，我们将左指针右移一位，略过一个相同数字，这对结果不会产生影响，因为我们只是去掉了一个相同的，然后对剩余的部分继续用二分查找法，在最坏的情况下，比如数组所有元素都相同，时间复杂度会升到O(n)

# reference
[[LeetCode] Find Minimum in Rotated Sorted Array II 寻找旋转有序数组的最小值之二][1]

[1]: http://www.cnblogs.com/grandyang/p/4040438.html