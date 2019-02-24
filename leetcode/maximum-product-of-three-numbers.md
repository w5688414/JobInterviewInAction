# problem
>Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
```
Input: [1,2,3]
Output: 6
```
Example 2:
```
Input: [1,2,3,4]
Output: 24
```
Note:

1. The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
2. Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.

# codes
```
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int sum=nums[0]*nums[1]*nums[n-1];
        sum=max(sum,nums[n-1]*nums[n-2]*nums[n-3]);
        return sum;
    }
};
```

# analysis

题目的意思是：找出一个数组中三个数的乘积最大。

考虑正负数的情况。
如果全都是正数相乘比较大，就取三个最大值相乘即可。
如果负数的绝对值比较大，我们可以取绝对值最大的两个负数参与相乘，最后比较一下两种算法的乘积哪个大。

# reference
[leetcode 628 Maximum Product of Three Numbers](https://segmentfault.com/a/1190000013119538?utm_source=tag-newest)
