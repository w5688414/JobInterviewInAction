# problem
>Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
```
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
```
Note:
- 1 <= k <= len(nums) <= 16.
- 0 < nums[i] < 10000.

# codes
```
class Solution {
public:
    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum=accumulate(nums.begin(),nums.end(),0);
        if(sum%k!=0) return false;
        vector<bool> visted(nums.size(),false);
        return solve(nums,k,sum/k,0,0,visted);
    }
    
    bool solve(vector<int>& nums,int k,int target,int start,int curSum,vector<bool> &visited){
        if(k==1){
            return true;
        }
        if(curSum==target) return solve(nums,k-1,target,0,0,visited);
        for(int i=start;i<nums.size();i++){
            if(visited[i]){
                continue;
            }
            visited[i]=true;
            if(solve(nums,k,target,i+1,curSum+nums[i],visited)) return true;
            visited[i]=false;
        }
        return false;
        
    }
};
```

# analysis
>这道题目我没有啥想法，一看到题目感觉很难下手，后面发现就是一个深度优先搜索，然后需要加visited数组标记是否访问过，然后加了一个curSum来记录当前的求和。写完之后还是发现有好多细节蛮有意思，比如if(curSum==target),我们就找到了一个符合条件的解，然后继续找下一个解，即k-1。就是不容易想到。

# reference
[[LeetCode] Partition to K Equal Sum Subsets 分割K个等和的子集][1]

[1]: https://www.cnblogs.com/grandyang/p/7733098.html