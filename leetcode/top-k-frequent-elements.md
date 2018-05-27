# problem
>Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# codes
```
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(auto num:nums){
            mp[num]++;
        }
        vector<vector<int>> buckets(nums.size()+1);
        for(auto item:mp){
            buckets[item.second].push_back(item.first);
        }
        reverse(buckets.begin(),buckets.end());
        vector<int> result;
        for(auto &bucket:buckets){
            for(auto i:bucket){
                result.push_back(i);
                if(result.size()==k){
                    return result;
                }
            }
        }
        return result;
    }
};
```

# analysis
>这道题说实话我也不会，首先建立一个map，然后将map的key value值互换，放进桶里面，然后逆转桶，这样一个一个从桶里面取数据，就是前k个了。
```
input: nums = [ 1,1,1,1,1 ]
map[1] = 5

then bucket index range should be 0~5, that why bucket size is nums.size() +1.
```
# reference
[347. Top K Frequent Elements][1]

[1]: https://leetcode.com/problems/top-k-frequent-elements/discuss/81676/C++-O(nlogk)-and-O(n)-solutions


