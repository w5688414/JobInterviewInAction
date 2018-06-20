# problem
>Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
```
nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
```
Example 2:
```
nums: [1,2,4,8]

Result: [1,2,4,8]
```

# codes
```
class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        vector<int> result;
        sort(nums.begin(),nums.end());
        vector<int> dp(nums.size(),0);
        vector<int> parent(nums.size(),0);
        int mx=0;
        int mx_idx=0;
        for(int i=nums.size()-1;i>=0;i--){
            for(int j=i;j<nums.size();j++){
                if(nums[j]%nums[i]==0&&dp[i]<dp[j]+1){
                    dp[i]=dp[j]+1;
                    parent[i]=j;
                    if(mx<dp[i]){
                        mx=dp[i];
                        mx_idx=i;
                    }
                }
            }
        }
        for(int i=0;i<mx;i++){
            result.push_back(nums[mx_idx]);
            mx_idx=parent[mx_idx];
        }
        return result;
    }
 
};
```

# analysis
>这道题目我用了DFS方法，发现超时了，最后一个测试样例超时，不过我觉得没有遗憾了。最好的方法还是动态规划，这道题dp[i]表示数字nums[i]位置最大可整除的子集合的长度，还需要一个一维数组parent，来保存上一个能整除的数字的位置，两个整型变量mx和mx_idx分别表示最大子集合的长度和起始数字的位置；
>我们可以从后往前遍历数组，对于某个数字再遍历到末尾，在这个过程中，如果nums[j]能整除nums[i], 且dp[i] < dp[j] + 1的话，更新dp[i]和parent[i]，如果dp[i]大于mx了，还要更新mx和mx_idx，最后循环结束后，我们来填res数字，根据parent数组来找到每一个数字。
这里需要给数组排序，有序的方便处理一点。


# reference
[[LeetCode] Largest Divisible Subset 最大可整除的子集合][1]

[1]: https://www.cnblogs.com/grandyang/p/5625209.html