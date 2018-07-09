# problem
>Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
```
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
```
Example 2:
```
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
```
Note:
1. The length sum of the given matchsticks is in the range of 0 to 10^9.
2. The length of the given matchstick array will not exceed 15.

# codes

## s1
```
class Solution {
public:
    bool makesquare(vector<int>& nums) {
        if(nums.empty()||nums.size()<4) return false;
        int sum=accumulate(nums.begin(),nums.end(),0);
        if(sum%4!=0) return false;
        vector<int> sums(4,0);
        sort(nums.rbegin(),nums.rend());
        return solve(nums,sum/4,0,sums);
    }
    bool solve(vector<int>& nums,int target,int pos,vector<int>& sums){
        if(pos>=nums.size()){
            return (sums[0]==target&&sums[1]==target&&sums[2]==target);
        }
        for(int i=0;i<4;i++){
            if(sums[i]+nums[pos]>target) continue;
            sums[i]+=nums[pos];
            if(solve(nums,target,pos+1,sums)) return true;
            sums[i]-=nums[pos];
        }
        return false;
    }
};
```


# analysis
>建立一个长度为4的数组sums来保存每个边的长度和，我们希望每条边都等于target，数组总和的四分之一。然后我们遍历sums中的每条边，我们判断如果加上数组中的当前数字大于target，那么我们跳过，如果没有，我们就加上这个数字，然后对数组中下一个位置调用递归，如果返回为真，我们返回true，否则我们再从sums中对应位置将这个数字减去继续循环.

## reference
[[LeetCode] Matchsticks to Square 火柴棍组成正方形][1]

[1]: http://www.cnblogs.com/grandyang/p/6238425.html

