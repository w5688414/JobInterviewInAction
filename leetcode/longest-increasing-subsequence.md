# problem
>Given an unsorted array of integers, find the length of longest increasing subsequence.
Example:
```
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
```
Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

# codes
```
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.size()==0){
            return 0;
        }
        vector<int> dp(nums.size(),1);
        int max_len=1;
        for(int i=1;i<nums.size();i++){
            for(int j=0;j<i;j++){
                if(nums[i]>nums[j]){
                    dp[i]=max(dp[j]+1,dp[i]);
                }
            }
            max_len=max(max_len,dp[i]);
        }
        return max_len;
    }
};
```

# analysis
>这题用了动态规划的方法
对于每一个元素，都有可能跟前面的序列构成一个较长的上升序列，或者跟后面的序列构成一个较长的上升序列
1）对于10这个元素，它是第一个，所以它构成的最长上升子序列长度为1；
2）对于9这个元素，前面没有比它小的，所以它构成的最长上升子序列长度为1；
3）对于2这个元素，遍历前面的10和9，没有比它小的，所以它构成的最长上升子序列长度为1；
4）对于5这个元素，遍历前面的10，9，2，发现2比它小，所以能和2构成最长上升子序列，2的最长上升子序列的长度为1，所以5的最长上升子序列长度是1+1=2；
5）对于3这个元素，遍历前面的10，9，2，5，发现2比它小，所以能和2构成最长上升子序列，2的最长上升子序列的长度为1，所以3的最长上升子序列长度是1+1=2；
6）对于7这个元素，遍历前面10，9，2，5，3，发现2，5，3，比它小，找2，5，3谁的最长上升子序列长度最长，最长值加1，得到了长度2+1=3；
7）对于101这个元素，遍历前面的10，9，2，5，3，7，发现都比它小，找前面的10，9，2，5，3，7谁的最长上升子序列最长，发现7的子序列长度最大，最大值加1，得到长度4.
8）对于18这个元素，遍历前面的10，9，2，5，3，7，101，发现10，9，2，5，3，7比它小，找这几个元素谁的最长上升子序列最长，最长值3加1，得到了3+1=4；


# reference
[leetcode 300. Longest Increasing Subsequence][1]
[LeetCode 300. Longest Increasing Subsequence（最长递增子序列）][2]

[1]: https://www.cnblogs.com/iwangzheng/p/5728838.html
[2]: https://blog.csdn.net/jmspan/article/details/51171519

