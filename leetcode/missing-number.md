# problem
>Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
```
Input: [3,0,1]
Output: 2
```
Example 2:
```
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


# codes
```
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sum=0;
        int n=nums.size();
        for(auto a:nums){
            sum+=a;
        }
        return 0.5*n*(n+1)-sum;
    }
};
```

# analysis
>等差数列求和，然后减去整个数组的和，相减就是剩下的了。

# reference
[[LeetCode] Missing Number 丢失的数字][1]

[1]: https://www.cnblogs.com/grandyang/p/4756677.html