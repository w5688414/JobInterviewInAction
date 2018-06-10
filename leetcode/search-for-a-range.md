# problem
>Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```
Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```
    
# codes
```
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.size()==0){
            return {-1,-1};
        }
       int left_bound=extremeInsertionIndex(nums,target,true);
        if(left_bound==nums.size()||nums[left_bound]!=target){
            return {-1,-1};
        }
        int right_bound=extremeInsertionIndex(nums,target,false)-1;
        return {left_bound,right_bound};
    }
private:
    int extremeInsertionIndex(vector<int>& nums, int target,bool left){
        int low=0;
        int high=nums.size();
        while(low<high){
            int mid=(low+high)/2;
            if(target<nums[mid]||(left&&target==nums[mid])){
                high=mid;
            }else{
                low=mid+1;
            }
        }
        return low;
    }
};
```

# analysis
>时间复杂度为O(logn),空间复杂度为O(1)，我也写了一个版本的代码，并且AC过了，但是总感觉有问题，我这里又参考了别人的代码，用了两次binary search就行了，注意里面的search的写法，有点讲究，不然会遇见bug。不过真要自己写出这样的代码，还是有点难度的。

# reference
[34. Search for a Range][1]

[1]: https://leetcode.com/problems/search-for-a-range/solution/
