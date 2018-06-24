# problem
>Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:
```
Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
```
Example 2:
```
Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
```
Note:
1. The length of nums is at most 20000.
2. Each element nums[i] is an integer in the range [1, 10000].

# codes

```
class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        vector<int> sums(10001,0);
        for(auto num:nums){
            sums[num]+=num;
        }
        vector<int> dp(sums.size(),0);
        dp[1]=sums[1];
        for(int i=2;i<sums.size();i++){
            dp[i]=max(dp[i-1],dp[i-2]+sums[i]);
        }
        return dp[10000];
    }  
};
```

# analysis
>可能是自己水平不够的原因，这道题目没有想出来。然后看了别人的解，析发现解法好奇妙，我们首先统计每个数的求和，然后就可以转化成house robber的问题了，看来还是自己太年轻了。要努力努力。

# reference

[Delete and Earn问题及解法][1]
[[LeetCode] Delete and Earn 删除与赚取][2]

[1]: https://blog.csdn.net/u011809767/article/details/78779705
[2]: http://www.cnblogs.com/grandyang/p/8176933.html
