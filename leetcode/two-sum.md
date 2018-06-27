# problem
>Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

# codes

## s1
```
class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        map<int,int> mp;
        vector<int> res;
        for(int i=0;i<numbers.size();i++){
            mp[numbers[i]]=i;
        }
        for(int i=0;i<numbers.size();i++){
            int diff=target-numbers[i];
            if(mp.find(diff)!=mp.end()&&mp[diff]>i){
                res.push_back(i+1);
                res.push_back(mp[diff]+1);
                break;
            }
        }
       return res;
    }
};
```
## s2

```
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        for(int i=0;i<nums.size();i++){
            if(m.count(target-nums[i])){
                return {i,m[target-nums[i]]};
            }
            m[nums[i]]=i;
        }
        return {};
    }
};
```

# analysis
>我也想到了用map函数，但是没想到会用这种diff的方式进行比较，看来我的火候还不够。

s2方案本质还是一样，只是代码写的更简洁了。

# reference
[[编程题]two-sum][1]


[1]: https://www.nowcoder.com/questionTerminal/20ef0972485e41019e39543e8e895b7f