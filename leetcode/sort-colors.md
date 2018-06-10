# problem
>Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
Example:
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
Follow up:
- A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
- Could you come up with a one-pass algorithm using only constant space?

# codes
```
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low=0;
        int high=nums.size()-1;
        int i=0;
        while(i<=high){
            if(nums[i]>1){
                swap(nums[i],nums[high]);
                high--;
            }else if(nums[i]<1){
                swap(nums[i],nums[low]);
                i++;
                low++;
            }else{
                i++;    
            }
            
        }
    }
};

```

# analysis
>这道题我也不怎么会，看来还是答案好，后面需要多想，该睡觉了，怕猝死。

# reference
[75. Sort Colors][1]

[1]: https://leetcode.com/problems/sort-colors/discuss/134266/C++-beats-100