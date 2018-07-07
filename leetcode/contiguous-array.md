# problem
>Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
Example 1:
```
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
```
Example 2:
```
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
```
Note: The length of the given binary array will not exceed 50,000.

# codes
```
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n=nums.size();
        int res=0;
        unordered_map<int,int> m{{0,-1}};
        int sum=0;
        for(int i=0;i<n;i++){
            sum+= nums[i]==1 ? 1:-1;
            if(m.count(sum)){
                res=max(res,i-m[sum]);
            }else{
                m[sum]=i;
            }
        }
        return res;
    }
};
```

# analysis
>需要用到一个trick，遇到1就加1，遇到0，就减1，这样如果某个子数组和为0，就说明0和1的个数相等.这个我并没有想到，所以做不出来。
- 我们用一个哈希表建立子数组之和跟结尾位置的坐标之间的映射。如果某个子数组之和在哈希表里存在了，说明当前子数组减去哈希表中存的那个子数字，得到的结果是中间一段子数组之和，必然为0，说明0和1的个数相等，我们更新结果res

# reference
[[LeetCode] Contains Duplicate II 包含重复值之二][1]

[1]: http://www.cnblogs.com/grandyang/p/4539680.html