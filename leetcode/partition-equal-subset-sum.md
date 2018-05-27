# problem
>Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:
```
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```
Example 2:
```
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```

# codes
```
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum=accumulate(nums.begin(),nums.end(),0);
        if(sum&1){
            return false;
        }
        sum=sum/2;
        vector<bool> dp(sum+1,false);
        dp[0]=true;
        for(int x:nums){
            for(int i=sum;i>=x;i--){
                dp[i]=dp[i]||dp[i-x];
            }
        }
        return dp[sum]; 
    }
};

```

# analysis
- 这道题给了我们一个数组，问我们这个数组能不能分成两个非空子集合，使得两个子集合的元素之和相同。那么我们想，原数组所有数字和一定是偶数，不然根本无法拆成两个和相同的子集合，那么我们只需要算出原数组的数字之和，然后除以2，就是我们的target.
- 那么问题就转换为能不能找到一个非空子集合，使得其数字之和为target。
- 开始我想的是遍历所有子集合，算和，但是这种方法无法通过OJ的大数据集合。于是就可以用动态规划 Dynamic Programming。
- dp[i]表示数字i是否是原数组的任意个子集合之和，那么我们我们最后只需要返回dp[target]就行了。
- 初始化dp[0]为true，由于题目中限制了所有数字为正数，那么我们就不用担心会出现和为0或者负数的情况。
- 关键问题就是要找出状态转移方程，我们需要遍历原数组中的数字，对于遍历到的每个数字nums[i]，我们需要更新dp数组，要更新[nums[i], target]之间的值，那么对于这个区间中的任意一个数字j，如果dp[j - nums[i]]为true的话，那么dp[j]就一定为true，于是状态转移方程如下：
 dp[j] = dp[j] || dp[j - nums[i]]         (nums[i] <= j <= target)

# reference
[[编程题]palindrome-partitioning][1]
[[LeetCode] Partition Equal Subset Sum 相同子集和分割][2]

[1]: https://www.nowcoder.com/questionTerminal/f983806a2ecb4106a17a365a642a9632
[2]: https://www.cnblogs.com/grandyang/p/5951422.html