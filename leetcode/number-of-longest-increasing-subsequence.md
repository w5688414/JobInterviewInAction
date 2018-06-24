# problem
>Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
```
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
```
Example 2:
```
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
```
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.


# codes
```
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        vector<int> lens(nums.size(),1);
        vector<int> cnt(nums.size(),1);
        int maxLen=0;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    if(lens[i]==lens[j]+1){
                        cnt[i]+=cnt[j];
                    }else if(lens[i]<lens[j]+1){
                        lens[i]=lens[j]+1;
                        cnt[i]=cnt[j];
                    }
                }
            }
            maxLen=max(maxLen,lens[i]);
        }
        int res=0;
        for(int i=0;i<lens.size();i++){
            if(lens[i]==maxLen){
                res+=cnt[i];
            }
        }
        return res;
    }
};
```

# analysis
1. 用一个数组lens存储到这个数字位置最长的自增序列的长度;
2. 用一个数组cnt存储以这个数字为结尾的最长的递增序列的个数。

更新lens比较好更新：比较nums[i] 和 nums[j]的大小

更新cnt时需注意，需要比较lens[i] 和 lens[j]的大小

注意此时前提是nums[j] < nums[i]

1. 若lens[i] < lens[j] + 1 也就是说 lens[i] 记录的不为最长的，至少和lens[j]相比 , nums[i]的序列要短
此时我们更新lens[i] = lens[j] +1, cnt[i] = cnt[j]
2. 若lens[i] == lens[j] + 1，说明当前这个序列又是满足条件的最长子序列 所以 cnt[i] += cnt[j]


# reference
[673. Number of Longest Increasing Subsequence][1]

[1]: http://www.cnblogs.com/yaoyudadudu/p/9197364.html


