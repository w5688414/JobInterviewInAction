# problem
>We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
Example 1:
```
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
```
Note: The length of the input array will not exceed 20,000.

# codes
```
class Solution {
public:
    int findLHS(vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        map<int,int> m;
        for(int i=0;i<nums.size();i++){
            m[nums[i]]++;
        }
        int res=0;
        for(auto it=next(m.begin());it!=m.end();it++){
            auto pre=prev(it);
            if(it->first==pre->first+1){
                res=max(res,it->second+pre->second);
            }
        }
        return res;
    }
};
```

# analysis
>这道题要求两数相差不超过1的最大长度，做法很常规，这里没有想到map居然还有自动排序的功能，还能够这么遍历，看来语言不熟，做起来也比较麻烦。

# reference
[[LeetCode] Longest Harmonious Subsequence 最长和谐子序列][1]

[1]: http://www.cnblogs.com/grandyang/p/6896799.html
