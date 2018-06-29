# problem
>Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
```
Input: nums = [1,2,3,1], k = 3
Output: true
```
Example 2:
```
Input: nums = [1,0,1,1], k = 1
Output: true
```
Example 3:
```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

# codes
```
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int n=nums.size();
        unordered_map<int,int> m;
        for(int i=0;i<n;i++){
            if(m.find(nums[i])!=m.end()&&i-m[nums[i]]<=k){
                return true;
            }else{
                m[nums[i]]=i;
            }
        }
        return false;
    }
};
```

# analysis
>没想到用一个hash表存储每个值的索引就行了，看来我还是太嫩了，只能使用暴力。

# reference
[[LeetCode] Contains Duplicate II 包含重复值之二][1]

[1]: http://www.cnblogs.com/grandyang/p/4539680.html