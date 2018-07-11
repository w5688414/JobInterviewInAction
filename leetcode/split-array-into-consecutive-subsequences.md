# problem
>You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:
```
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
```
Example 2:
```
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
```
Example 3:
```
Input: [1,2,3,4,4,5]
Output: False
```
Note:
1. The length of the input is in range of [1, 10000]

# codes
```
class Solution {
public:
    bool isPossible(vector<int>& nums) {
        unordered_map<int,int> freq,need;
        for(int num:nums){
            freq[num]++;
        }
        for(int num:nums){
            if(freq[num]==0) continue;
            else if(need[num]>0){
                --need[num];
                ++need[num+1];
            }else if(freq[num+1]>0&&freq[num+2]>0){
                --freq[num+1];
                --freq[num+2];
                ++need[num+3];
            }else return false;
            --freq[num];
        }
        return true;
    }
};
```

# analysis
>我们使用两个哈希表map，第一个map用来建立数字和其出现次数之间的映射freq，第二个用来建立可以加在某个连续子序列后的数字及其可以出现的次数之间的映射need。
我并没有做出来，学习一下。

# reference
[[LeetCode] Split Array into Consecutive Subsequences 将数组分割成连续子序列][1]

[1]: http://www.cnblogs.com/grandyang/p/7525821.html