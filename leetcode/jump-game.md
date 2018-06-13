# problem
>Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A =[2,3,1,1,4], returntrue.

A =[3,2,1,0,4], returnfalse.

# codes
```
class Solution {
public:
    bool canJump(int A[], int n) {
        int max_val=0; //max_val标记能跳到的最远处。
        for(int i=0;i<n&&i<=max_val;i++){ //max_val>=i表示此时能跳到i处，0<=i<n表
            max_val=max(max_val,A[i]+i);  //示扫描所有能到达的点，在改点处能跳到的最远处。
        }
        if(max_val<n-1){ //如果最后跳的最远的结果大于等于n-1，那么满足,能跳到最后，否则，不能。
            return false;
        }
        return true;
    }
  
};
```
```
class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<int> dp(nums.size(),0);
        dp[0]=nums[0];
        for(int i=1;i<nums.size();i++){
            dp[i]=max(dp[i-1],nums[i-1])-1;
            if(dp[i]<0){
                return false;
            }
        }
        return dp[nums.size()-1]>=0;
    }
};
```

# analysis
>分析见注释
第二个解法是动态规划的解法，dp[i]表示到达i时剩余的步数，当前位置的剩余步数和当前位置的跳力较大的那个数决定了当前能到的最远距离。而下一个位置的剩余步数就等于较大值减去1，因为需要花费一个跳力到达下一个位置。状态转移方程为：
dp[i]=max(dp[i-1],nums[i-1])-1;

# reference
[[编程题]jump-game][1]
[[LeetCode] Jump Game 跳跃游戏][2]

[1]: https://www.nowcoder.com/questionTerminal/a2d856f493424a748bb7c9c1126e8d8d
[2]: http://www.cnblogs.com/grandyang/p/4371526.html
