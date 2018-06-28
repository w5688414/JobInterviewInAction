# problem
>Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

# codes

## s1
```
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> res;
        int l=0;
        int r=numbers.size()-1;
        while(l<r){
            int sum=numbers[l]+numbers[r];
            if(sum==target){
                return {l+1,r+1};
            }else if(sum<target){
                l++;
            }else{
                r--;
            }
        }
        return res;
    }
};
```


# analysis
>开始写了一个O(n^2)的解法，后面查资料还有O(n)的解法，果断学习了，就是一个夹逼的过程。

# reference
[[LeetCode] Two Sum II - Input array is sorted 两数之和之二 - 输入数组有序][1]


[1]: http://www.cnblogs.com/grandyang/p/5185815.html