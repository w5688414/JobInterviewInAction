# problem
>Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
```
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
```
Example 2:
```
Input: [1,2,2,3,1,4,2]
Output: 6
```
Note:
- nums.length will be between 1 and 50,000.
- nums[i] will be an integer between 0 and 49,999.

# codes

```
class Solution {
public:
    int findShortestSubArray(vector<int>& nums) {
        unordered_map<int,int> m;
        unordered_map<int,pair<int,int>> pos;
        int degree=0;
        for(int i=0;i<nums.size();i++){
            m[nums[i]]++;
            if(m[nums[i]]==1){
                pos[nums[i]]={i,i};
            }else{
                pos[nums[i]].second=i;
            }
            degree=max(degree,m[nums[i]]);
        }
        int res=INT_MAX;
        for(auto count:m){
            if(degree==count.second){
                res=min(res,pos[count.first].second-pos[count.first].first+1);
            }
        }
        return res;
    }
};
```

# analysis
>用hash表存放次数，用另一个hash表存放该数值在数组的起始位置和结束位置。最后把degree的最大的几个数取出来，取最小长度就行了。

# reference

[[LeetCode] Degree of an Array 数组的度][1]

[1]: http://www.cnblogs.com/grandyang/p/7722949.html