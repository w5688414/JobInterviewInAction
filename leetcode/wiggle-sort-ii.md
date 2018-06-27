# problem
>Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:
```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
```
Example 2:
```
Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
```
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

# codes
```
class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n=nums.size();
        auto midptr=nums.begin()+n/2;
        nth_element(nums.begin(),midptr,nums.end());
        int mid=*midptr;
        // Index-rewiring.
        #define A(i) nums[(1+2*(i)) % (n|1)]
        int i=0;
        int j=0;
        int k=n-1;
        while(j<=k){
            if(A(j)>mid){
                swap(A(i++),A(j++));
            }else if(A(j)<mid){
                swap(A(j),A(k--));
            }else{
                j++;
            }
        }
    }
};
```

# analysis
>STL中的nth_element()方法的使用 通过调用nth_element(start, start+n, end) 方法可以使第n大元素处于第n位置（从0开始,其位置是下标为 n的元素），并且比这个元素小的元素都排在这个元素之前，比这个元素大的元素都排在这个元素之后，但不能保证他们是有序的。

这题的解法我也不知道，所以无可奉告，以后再研究一下。

# reference
[324. Wiggle Sort II][1]
[STL中的nth_element()方法的使用][2]

[1]: https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)+O(1)-after-median-Virtual-Indexing
[2]: https://blog.csdn.net/guofengzai/article/details/2574225