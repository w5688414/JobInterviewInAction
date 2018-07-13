# problem
>Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
Example:
```
Input:  [1,2,1,3,2,5]
Output: [3,5]
```
Note:

1. The order of the result is not important. So in the above example, [5, 3] is also correct.
2. Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
# codes
## s1
```
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int diff=0;
        for(int i=0;i<nums.size();i++){
            diff=diff^nums[i];
        }
        diff&=-diff;
        vector<int> res(2,0);
        for(int i=0;i<nums.size();i++){
            if(nums[i]&diff) res[0]^=nums[i];
            else res[1]^=nums[i];
        }
        return res;
    }
};
```

# analysis
- 们如果能想办法把原数组分为两个小数组，不相同的两个数字分别在两个小数组中，这样分别调用Single Number 单独的数字的解法就可以得到答案。
>首先我们先把原数组全部异或起来，那么我们会得到一个数字，这个数字是两个不相同的数字异或的结果，我们取出其中任意一位为‘1’的位，为了方便起见，我们用 a &= -a 来取出最右端为‘1’的位，然后和原数组中的数字挨个相与，那么我们要求的两个不同的数字就被分到了两个小组中，分别将两个小组中的数字都异或起来，就可以得到最终结果了.

这道题需要对位运算非常熟悉才行，不然就拿它没办法。

# reference
[[LeetCode] Single Number III 单独的数字之三][1]


[1]: http://www.cnblogs.com/grandyang/p/4741122.html