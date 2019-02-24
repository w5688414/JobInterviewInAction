# problem
>Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
```
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
```
Note:
1. 1 <= k <= n <= 30,000.
2. Elements of the given array will be in the range [-10,000, 10,000].

# codes
```
class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        for(int i=1;i<nums.size();i++){
            nums[i]+=nums[i-1];
        }
        double avg=0;
        int i=0;
        double res=INT_MIN;
        while(i+k-1<nums.size()){
            if(i==0){
                avg=nums[k-1]/(double)k;
            }else{
                avg=(nums[i+k-1]-nums[i-1])/(double)k;
            }
            res=max(res,avg);
            i++;
        }
        return res;
    }
};
```

# analysis
>

# reference
[[LeetCode] Maximum Average Subarray I 子数组的最大平均值][1]

[1]: https://www.cnblogs.com/grandyang/p/7294585.html
