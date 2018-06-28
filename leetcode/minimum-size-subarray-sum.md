# problem
>Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:
```
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

# codes
```
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.empty()){
            return 0;
        }
        int i=0;
        int j=i+1;
        int sum=nums[i];
        
        int m=nums.size();
        int len=m+1;
        while(j<m){
            while(sum<s&&j<m){
                sum+=nums[j];
                j++;
            }
            while(sum>=s){
                len=min(len,j-i);
                sum-=nums[i];
                i++;
            }
        }
        return len==m+1 ? 0:len;
    }
};
```
# analysis
>定义两个指针left和right，分别记录子数组的左右的边界位置，然后我们让right向右移，直到子数组和大于等于给定值或者right达到数组末尾，此时我们更新最短距离，并且将left像右移一位，然后再sum中减去移去的值，然后重复上面的步骤，直到right到达末尾，且left到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值。

# reference
[[LeetCode] Minimum Size Subarray Sum 最短子数组之和][1]

[1]: http://www.cnblogs.com/grandyang/p/4501934.html