# problem
> Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
Example:
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

# codes
```
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(),1);
        for(int i=1;i<nums.size();i++){
            result[i]=nums[i-1]*result[i-1];
        }
        int right=1;
        for(int i=nums.size()-1;i>=0;i--){
            result[i]=right*result[i];
            right=right*nums[i];
        }
        return result;
    }
};
```

# analysis
>对于某一数字，如果我们知道其前面所有数字的乘积，同时也知道后面所有的乘积，那么二者就是我们要的结果。因此我们创建一个数组来保存前面连乘的结果，前向遍历一次，后向遍历一次就行了。

# reference
[[LeetCode] Product of Array Except Self 除本身之外的数组之积][1]

[1]: https://www.cnblogs.com/grandyang/p/4650187.html

