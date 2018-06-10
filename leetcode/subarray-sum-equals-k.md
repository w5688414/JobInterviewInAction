# problem
>Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
Example 1:
```
Input:nums = [1,1,1], k = 2
Output: 2
```
Note:
1.The length of the array is in range [1, 20,000].
2.The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

# codes
```
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int sum=0;
        map<int,int> mp;
        int count=0;
        mp[0]++;
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
            count+=mp[sum-k];
            mp[sum]++;  
        }
        return count;
    }
};
```

# analysis
>这个题目的暴力破解方法我都没想到，跑偏了，原来是以每一个位置为起点进行求和就是暴力破解。后面的优化方法是用一个map存起来，mp[0]的初始值为1，用于然后mp记录的是前m项的求和，mp[sum-k]如果为1，表明存在一个连续子序列的值为k，这需要找个test case模拟一下就行了。

# reference
[[LeetCode] Subarray Sum Equals K 子数组和为K][1]
[560. Subarray Sum Equals K][2]

[1]: https://www.cnblogs.com/grandyang/p/6810361.html
[2]: https://leetcode.com/problems/subarray-sum-equals-k/discuss/102121/C++-prefix-sum-+-map
