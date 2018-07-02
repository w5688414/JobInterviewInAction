# problem
>Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

Example 1:
```
Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
```
Example 2:
```
Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
```

Note:

- The length of nums will be in the range [0, 10000].
- Each element nums[i] will be an integer in the range [-1000, 1000].

# codes
```
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum=accumulate(nums.begin(),nums.end(),0);
        int curSum=0;
        int n=nums.size();
        for(int i=0;i<n;i++){
            if(sum-nums[i]==curSum*2) return i;
            curSum+=nums[i];
        }
        return -1;
    }
};
```

# analysis
>这道题我用左右指针法试了一下，发现数组里面包含负数就不行了，看来我还是太年轻了，这是别人的解法，很简单，我觉得不容易想到。

# reference
[[LeetCode] Find Pivot Index 寻找中枢点][1]

[1]: http://www.cnblogs.com/grandyang/p/7865693.html