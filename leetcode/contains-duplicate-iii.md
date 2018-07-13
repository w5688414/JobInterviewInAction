# problem
>Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
Example 1:
```
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
```
Example 2:
```
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
```
Example 3:
```
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
```

# codes
```
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        map<long long,int> m;
        int j=0;
        for(int i=0;i<nums.size();i++){
            if(i-j>k) m.erase(nums[j++]);
            auto a=m.lower_bound((long long)nums[i]-t);
            if(a!=m.end()&&abs(a->first-nums[i])<=t){
                return true;
            }
            m[nums[i]]=i;
        }
        return false;
    }
};
```

# analysis
- 这里需要两个指针i和j，刚开始i和j都指向0，然后i开始向右走遍历数组，如果i和j之差大于k，且m中有nums[j]，则删除并j加一。这样保证了m中所有的数的下标之差都不大于k.
- 我们用map数据结构的lower_bound()函数来找一个特定范围，就是大于或等于nums[i] - t的地方，所有小于这个阈值的数和nums[i]的差的绝对值会大于t.
- 然后检测后面的所有的数字，如果数的差的绝对值小于等于t，则返回true.

# reference
[[LeetCode] Contains Duplicate III 包含重复值之三][1]

[1]: http://www.cnblogs.com/grandyang/p/4545261.html